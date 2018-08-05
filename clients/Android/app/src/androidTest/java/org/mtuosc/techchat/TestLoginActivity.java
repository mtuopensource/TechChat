package org.mtuosc.techchat;



import android.support.design.widget.TextInputEditText;
import android.support.test.espresso.ViewAssertion;
import android.support.test.espresso.matcher.BoundedMatcher;
import android.support.test.filters.MediumTest;
import android.support.test.rule.ActivityTestRule;
import android.support.test.runner.AndroidJUnit4;
import android.view.View;
import org.hamcrest.Description;
import org.hamcrest.Matcher;
import org.hamcrest.TypeSafeMatcher;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mtuosc.techchat.activity.LoginActivity;



import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;

import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static org.hamcrest.CoreMatchers.not;


@RunWith(AndroidJUnit4.class)
@MediumTest
public class TestLoginActivity {

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

    @Rule
    public ActivityTestRule<LoginActivity> loginActivityTest = new ActivityTestRule<>(LoginActivity.class);

    @Test public void testErrorShown(){
        onView(withId(R.id.email_sign_in_button)).perform(click());

        onView(withId(R.id.login_email_input)).check(matches(hasErrorText()));
        onView(withId(R.id.login_password_input)).check(matches(hasErrorText()));

    }

}
