package org.mtuosc.techchat.activity;


import android.content.Intent;

import android.content.Context;

import android.os.Parcel;
import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.Toast;


import com.goebl.david.Response;

import org.json.JSONException;
import org.json.JSONObject;
import org.mtuosc.techchat.utils.EmailPasswordValidator;
import org.mtuosc.techchat.R;
import org.mtuosc.techchat.UserData;
import org.mtuosc.techchat.UserDataStorage;
import org.mtuosc.techchat.asynctasks.AsyncApiResponse;
import org.mtuosc.techchat.asynctasks.UserAuthenticator;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * A login screen that offers login via email/password.
 */
public class LoginActivity extends BaseInternetActivity implements AsyncApiResponse<Response<JSONObject>> {
    /**
     * regular expression found at https://en.wikipedia.org/wiki/Email_address#Valid_email_addresses
     */
    private EmailPasswordValidator validator = new EmailPasswordValidator();

    private TextInputLayout emailTextWrapper;
    private TextInputLayout passwordTextWrapper;
    private ProgressBar loginProgress;
    private Button submitButton;
    private UserDataStorage dataStorage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        setTheme(R.style.AppTheme_NoActionBar); // must come before onCreate, for  the splash screen to work
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_base);

        dataStorage = new UserDataStorage(getSharedPreferences("TechChat", Context.MODE_PRIVATE));
        UserData userData = dataStorage.getCurrentUserData();
        if (userData.userExists()) {
            Intent moveToBoards = new Intent(this, BoardsActivity.class);
            //moveToBoards.putExtra("cookie", userData.getCookie());
            startActivity(moveToBoards);
            finish();
        }

        // check the shared preference for user data, auto login

        emailTextWrapper = findViewById(R.id.email_login_wrapper);
        passwordTextWrapper = findViewById(R.id.password_login_wrapper);
        loginProgress = findViewById(R.id.login_progress);
        submitButton = findViewById(R.id.email_sign_in_button);
    }

    /**
     * Moves the user to the create user activity
     * @param view this should be the text view
     */
    public void moveToUserCreation(View view) {
        Intent userCreation = new Intent(this, CreateUserActivity.class);
        startActivity(userCreation);
    }

    public void authenticateUser(View view) {
        if (hasInternet()) {
            String email = emailTextWrapper.getEditText().getText().toString();
            String password = passwordTextWrapper.getEditText().getText().toString();

            if (showedInputErrorsToUser(email, password))
                return; // don't submit the form

            // send the form to backend

            UserAuthenticator authenticator = new UserAuthenticator(email, password, this);

            loginProgress.setVisibility(View.VISIBLE);
            submitButton.setText("");

            authenticator.execute();
        }else
            showConnectionWarning();

    }

    private boolean showedInputErrorsToUser(String email, String password){
        boolean errorShown = false;
        if (!validator.isEmailValid(email)) {
            emailTextWrapper.getEditText().setError("Invalid Email");
            errorShown = true;
        }
        if (!validator.isPasswordValid(password)){
            errorShown = true;
            passwordTextWrapper.getEditText().setError("Not a Valid Password");
        }

        return errorShown;
    }


    @Override
    public void taskCompleted(Response<JSONObject> result) {
        if (result.getStatusCode() == 200){
            JSONObject tokenJSON = result.getBody();
            try {
                String refreshToken = tokenJSON.getString("refresh");
                String accessToken = tokenJSON.getString("access");
                String email = emailTextWrapper.getEditText().getText().toString();
                String password = passwordTextWrapper.getEditText().getText().toString();
                
                UserData user = UserData.getInstance();
                user.setRefreshToken(refreshToken);
                user.setAccessToken(accessToken);
                user.setUsername(email);
                user.setPassword(password);
                dataStorage.saveUserData(user);


                Intent moveToBoards = new Intent(this, BoardsActivity.class);
                startActivity(moveToBoards);

            } catch (JSONException e) {
                e.printStackTrace();
            }
            finish(); // prevents users going back

        }
        else {
            if (result.getStatusCode() == 400)
                Toast.makeText(this, R.string.bad_credentials, Toast.LENGTH_SHORT).show();
            else
                Toast.makeText(this, "Server Error", Toast.LENGTH_LONG).show();
        }
        loginProgress.setVisibility(View.INVISIBLE);
        submitButton.setText(R.string.action_sign_in);
    }

    //TODO: Make this into a helper class or something
    public static String getCookieData(String cookieSession) {
        final String regex = "(?<=sessionid=)(\\w+)";

        final Pattern pattern = Pattern.compile(regex);
        final Matcher matcher = pattern.matcher(cookieSession);
        matcher.find();
        return matcher.group(0);
    }
}

