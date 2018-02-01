package org.mtuosc.techchat.activity;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.widget.TextView;

import org.mtuosc.techchat.R;

/**
 * Created by ryan on 1/27/18.
 */

public class CreateUserActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.create_user_layout);
        TextView termsOfServ = createTermsOfServiceText();
    }
    private TextView createTermsOfServiceText(){
        TextView termsOfServ = findViewById(R.id.terms_of_service);
        termsOfServ.setText(Html.fromHtml("<p> By Tapping the button above, you subscribe yourself to our " +
                "<a href=\"http://google.com\">Terms of Service</a> and our <a href=\"https://google.com\">Privacy Policy</a> </p>"));
        termsOfServ.setMovementMethod(LinkMovementMethod.getInstance());
        return termsOfServ;
    }
}
