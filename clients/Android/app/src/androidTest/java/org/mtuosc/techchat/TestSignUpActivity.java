package org.mtuosc.techchat;


import android.support.test.rule.ActivityTestRule;
import android.support.test.runner.AndroidJUnit4;

import org.hamcrest.CoreMatchers;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mtuosc.techchat.activity.CreateUserActivity;
import org.mtuosc.techchat.testutil.MatcherUtil;

import static android.support.test.espresso.Espresso.closeSoftKeyboard;
import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.typeText;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.RootMatchers.withDecorView;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.core.IsNot.not;

@RunWith(AndroidJUnit4.class)
public class TestSignUpActivity {


    @Rule
    public ActivityTestRule<CreateUserActivity>
            createUserActivityTest = new ActivityTestRule<>(CreateUserActivity.class);

    @Test
    public void testMismatchedPasswords() {
        // we don't want an error from the email input, so let add a random email into it
        onView(withId(R.id.signup_email_input)).perform(typeText("random@random.com"));


        // input two different string into the password fields
        onView(withId(R.id.signup_password_input)).perform(typeText("Password"));
        closeSoftKeyboard(); // helps the test find the input
        onView(withId(R.id.signup_confirm_input)).perform(typeText("NotTheSamePassword"));
        closeSoftKeyboard();

        // click the signup button
        onView(withId(R.id.signup_button)).perform(click());

        // check for the error message
        onView(withId(R.id.signup_confirm_input))
                .check(matches(MatcherUtil.hasErrorText()));


    }


    /**
     * This test when the user tries to signup with an already used email
     */
    @Test
    public void testFailedSignup() {
        // enter in the test account email
        onView(withId(R.id.signup_email_input)).perform(typeText("test@mtu.edu"));
        closeSoftKeyboard();

        // enter in test password
        onView(withId(R.id.signup_password_input)).perform(typeText("test"));
        onView(withId(R.id.signup_confirm_input)).perform(typeText("test"));

        // click the signup button
        onView(withId(R.id.signup_button)).perform(click());

        // find the toast error message
        onView(withText("Email is already taken"))
                .inRoot(withDecorView(not(CoreMatchers.is(
                        createUserActivityTest.getActivity().getWindow().getDecorView()
                )))).check(matches(isDisplayed()));
    }

}
