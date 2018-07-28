package org.mtuosc.techchat.activity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.goebl.david.Response;

import org.json.JSONObject;
import org.mtuosc.techchat.UserData;
import org.mtuosc.techchat.UserDataStorage;
import org.mtuosc.techchat.asynctasks.AsyncApiResponse;
import org.mtuosc.techchat.utils.EmailPasswordValidator;
import org.mtuosc.techchat.R;
import org.mtuosc.techchat.asynctasks.SignUpUserTask;

/**
 * Created by ryan on 1/27/18.
 */

public class CreateUserActivity extends BaseInternetActivity implements AsyncApiResponse<Response<JSONObject>> {
    private EditText confirmEditText;
    private EditText passwordEditText;
    private EditText emailEditText;

    private EmailPasswordValidator validator = new EmailPasswordValidator();
    private SignUpUserTask signUpTask;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.create_user_layout);
        TextView termsOfServ = createTermsOfServiceText();

        emailEditText = ((TextInputLayout) findViewById(R.id.signup_email)).getEditText();
        passwordEditText = ((TextInputLayout) findViewById(R.id.signup_password)).getEditText();
        confirmEditText = ((TextInputLayout) findViewById(R.id.signup_confirm)).getEditText();

    }
    private TextView createTermsOfServiceText(){
        TextView termsOfServ = findViewById(R.id.terms_of_service);
        // TODO: Find cleaner solution for external links
        termsOfServ.setText(Html.fromHtml("<p> By Tapping the button above, you subscribe yourself to our " +
                "<a href=\"http://google.com\">Terms of Service</a> and our <a href=\"https://google.com\">Privacy Policy</a> </p>"));
        termsOfServ.setMovementMethod(LinkMovementMethod.getInstance());
        return termsOfServ;
    }

    public void signUpUser(View view) {
        if (hasInternet()) {
            String email = emailEditText.getText().toString();
            if (passwordsMatch() && validator.isEmailValid(email)) {
                String password = passwordEditText.getText().toString();
                signUpTask = new SignUpUserTask(email, password, this);
                signUpTask.execute();
            }
        }else
            showConnectionWarning();
    }

    private boolean passwordsMatch() {
        String confirm = confirmEditText.getText().toString();
        String password = passwordEditText.getText().toString();
        if (!confirm.equals(password)){
            confirmEditText.setError("Passwords do not match");
            return false;
        }
        return true;
    }

    @Override
    public void taskCompleted(Response<JSONObject> result) {
        if (result.getStatusCode() == 201 || result.getStatusCode() == 200){
            String cookieSession = result.getHeaderField("Set-Cookie");
            String cookie = LoginActivity.getCookieData(cookieSession);

            //saving cookie to file
            UserDataStorage storage = new UserDataStorage(getSharedPreferences("TechChat", Context.MODE_PRIVATE));
            storage.saveUserData(new UserData(cookie));

            // Move user to boards activity
            Intent moveToBoards = new Intent(this, BoardsActivity.class);
            moveToBoards.putExtra("cookie", cookie);
            startActivity(moveToBoards);

        }else{
            Toast.makeText(this, "Server Error", Toast.LENGTH_SHORT).show();
        }
    }
}
