package org.mtuosc.techchat.testutil;

import android.support.design.widget.TextInputEditText;
import android.support.test.espresso.matcher.BoundedMatcher;
import android.view.View;

import org.hamcrest.Description;
import org.hamcrest.Matcher;

public class MatcherUtil {

    public static Matcher<View> hasErrorText(){
        return new BoundedMatcher<View, TextInputEditText>(TextInputEditText.class) {

            @Override
            public void describeTo(Description description) {
                description.appendText("has no error text: ");
            }

            @Override
            protected boolean matchesSafely(TextInputEditText item) {
                return item.getError() != null;
            }
        };
    }
}
