package org.mtuosc.techchat.activity;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import org.mtuosc.techchat.R;

/**
 * Created by ryan on 1/27/18.
 */

public class CreateUserActivity extends AppCompatActivity {
    EditText confirmEditText;
    EditText passwordEditText;
    EditText email;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.create_user_layout);
        TextView termsOfServ = createTermsOfServiceText();

        email = ((TextInputLayout) findViewById(R.id.signup_email)).getEditText();
        passwordEditText = ((TextInputLayout) findViewById(R.id.signup_password)).getEditText();
        confirmEditText = ((TextInputLayout) findViewById(R.id.signup_confirm)).getEditText();

    }
    private TextView createTermsOfServiceText(){
        TextView termsOfServ = findViewById(R.id.terms_of_service);
        termsOfServ.setText(Html.fromHtml("<p> By Tapping the button above, you subscribe yourself to our " +
                "<a href=\"http://google.com\">Terms of Service</a> and our <a href=\"https://google.com\">Privacy Policy</a> </p>"));
        termsOfServ.setMovementMethod(LinkMovementMethod.getInstance());
        return termsOfServ;
    }

    public void signUpUser(View view) {
        if (passwordsMatch()){
            //TODO send the request to the server
        }else
            confirmEditText.setError("Passwords Do Not Match");


    }

    private boolean passwordsMatch() {
        String confirm = confirmEditText.getText().toString();
        String password = passwordEditText.getText().toString();
        return confirm.equals(password);
    }
}
