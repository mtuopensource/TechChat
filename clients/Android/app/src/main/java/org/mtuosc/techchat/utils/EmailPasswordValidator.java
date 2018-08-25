package org.mtuosc.techchat.utils;

import android.support.annotation.NonNull;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by ryan on 2/4/18.
 */

public class EmailPasswordValidator {
    private static final String EMAIL_PATTERN_EXPRESS = "^[a-zA-Z0-9#_~!$&'()*+,;=:.\"(),:;<>@\\[\\]\\\\]+@[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)*$";
    private Pattern emailPattern = Pattern.compile(EMAIL_PATTERN_EXPRESS);

    public boolean isEmailValid(String email){
        Matcher emailMatcher = emailPattern.matcher(email);
        return emailMatcher.matches();
    }

    public boolean isPasswordValid(String password){
        // TODO add more logic if password must meet a requirement
        return !password.equalsIgnoreCase("");
    }
}
