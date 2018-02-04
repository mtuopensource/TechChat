package org.mtuosc.techchat.activity;


import android.content.Intent;

import android.content.Context;
import android.net.ConnectivityManager;

import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.Toast;



import java.util.regex.Matcher;
import java.util.regex.Pattern;


import org.mtuosc.techchat.EmailPasswordValidator;
import org.mtuosc.techchat.R;
import org.mtuosc.techchat.UserAuthenticator;

/**
 * A login screen that offers login via email/password.
 */
public class LoginActivity extends AppCompatActivity {
    /**
     * regular expression found at https://en.wikipedia.org/wiki/Email_address#Valid_email_addresses
     */
    private EmailPasswordValidator validator = new EmailPasswordValidator();

    private TextInputLayout emailTextWrapper;
    private TextInputLayout passwordTextWrapper;
    private ProgressBar loginProgress;
    private Button submitButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_base);



        // check the shared preference for user data, auto login

        emailTextWrapper = findViewById(R.id.email_login_wrapper);
        passwordTextWrapper = findViewById(R.id.password_login_wrapper);
        loginProgress = findViewById(R.id.login_progress);
        submitButton = findViewById(R.id.email_sign_in_button);
    }

    private boolean isNetworkConnected() {
        ConnectivityManager cm = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
        return cm.getActiveNetworkInfo() != null;
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
        String email = emailTextWrapper.getEditText().getText().toString();
        String password = passwordTextWrapper.getEditText().getText().toString();
        if(showedErrorsToUser(email, password))
            return; // don't submit the form

        // send the form to backend
        UserAuthenticator authenticator = new UserAuthenticator("http://141.219.197.116:8000", email, password);

        loginProgress.setVisibility(View.VISIBLE);
        submitButton.setText("");

        authenticator.startLogin();
        if (authenticator.isAuthenticated()){
            // save data to the shared preference
            Toast.makeText(this, "You're Logged in", Toast.LENGTH_SHORT).show();
        }else {
            Toast.makeText(this, "Not a valid Email or Password", Toast.LENGTH_SHORT).show();
        }
        loginProgress.setVisibility(View.INVISIBLE);
        submitButton.setText(R.string.action_sign_in);
    }

    private boolean showedErrorsToUser(String email, String password){
        boolean errorShown = false;
        if (!validator.isEmailValid(email)) {
            emailTextWrapper.getEditText().setError("Invalid Email");
            errorShown = true;
        }
        if (validator.isPasswordValid(password)){
            errorShown = true;
            passwordTextWrapper.getEditText().setError("Not a Valid Password");
        }
        if (!isNetworkConnected()) {
            Toast.makeText(this, "No Network", Toast.LENGTH_SHORT).show();
            errorShown = true;
        }
        return errorShown;
    }




}

