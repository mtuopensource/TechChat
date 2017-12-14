package org.mtuosc.techchat.activity;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.annotation.TargetApi;
import android.content.pm.PackageManager;
import android.support.annotation.NonNull;
import android.support.design.widget.Snackbar;
import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;
import android.app.LoaderManager.LoaderCallbacks;

import android.content.CursorLoader;
import android.content.Loader;
import android.database.Cursor;
import android.net.Uri;
import android.os.AsyncTask;

import android.os.Build;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.text.TextUtils;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.inputmethod.EditorInfo;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.mtuosc.techchat.R;

import static android.Manifest.permission.READ_CONTACTS;

/**
 * A login screen that offers login via email/password.
 */
public class LoginActivity extends AppCompatActivity {
    /**
     * regular expression found at https://en.wikipedia.org/wiki/Email_address#Valid_email_addresses
     */
    private static final String EMAIL_PATTERN_EXPRESS = "^[a-zA-Z0-9#_~!$&'()*+,;=:.\"(),:;<>@\\[\\]\\\\]+@[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)*$";
    private Pattern emailPattern = Pattern.compile(EMAIL_PATTERN_EXPRESS);

    private TextInputLayout emailTextWrapper;
    private TextInputLayout passwordTextWrapper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        emailTextWrapper = findViewById(R.id.email_login_wrapper);
        passwordTextWrapper = findViewById(R.id.password_login_wrapper);
    }

    /**
     * Moves the user to the create user activity
     * @param view this should be the text view
     */
    public void moveToUserCreation(View view) {
        // TODO implement the user creation usecase
        Toast.makeText(this, "Moving to Create User", Toast.LENGTH_SHORT).show();
    }

    public void authenticateUser(View view) {
        String email = emailTextWrapper.getEditText().getText().toString();
        String password = passwordTextWrapper.getEditText().getText().toString();
        showedErrors(email, password);
    }

    private boolean showedErrors(String email, String password){
        boolean errorShown = false;
        if (!isEmailValid(email)) {
            emailTextWrapper.setError("Not a Valid Email");
            errorShown = true;
        }
        if (isPasswordValid(password)){
            errorShown = true;
            passwordTextWrapper.setError("Not a Valid Password");
        }
        return errorShown;
    }

    private boolean isPasswordValid(String password){
        return password.equalsIgnoreCase("");
    }

    private boolean isEmailValid(String email){
        Matcher emailMatcher = emailPattern.matcher(email);
        return emailMatcher.matches();
    }
}

