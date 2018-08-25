package org.mtuosc.techchat;

import android.support.test.espresso.intent.Intents;
import android.support.test.filters.MediumTest;
import android.support.test.rule.ActivityTestRule;
import android.support.test.runner.AndroidJUnit4;

import org.hamcrest.CoreMatchers;

import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import org.mtuosc.techchat.activity.BoardsActivity;
import org.mtuosc.techchat.activity.CreateUserActivity;
import org.mtuosc.techchat.activity.LoginActivity;
import org.mtuosc.techchat.testutil.MatcherUtil;


import static android.support.test.espresso.Espresso.closeSoftKeyboard;
import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;

import static android.support.test.espresso.action.ViewActions.typeText;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.intent.Intents.intended;
import static android.support.test.espresso.intent.matcher.IntentMatchers.hasComponent;
import static android.support.test.espresso.matcher.RootMatchers.withDecorView;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.CoreMatchers.not;


@RunWith(AndroidJUnit4.class)
@MediumTest
public class TestLoginActivity {


    @Rule
    public ActivityTestRule<LoginActivity>
            loginActivityTest = new ActivityTestRule<>(LoginActivity.class);

    @Before
    public void setUp() throws Exception{
        Intents.init();
    }

    @Test
    public void testErrorShown(){
        // click the submit button
        onView(withId(R.id.email_sign_in_button)).perform(click());

        // check for the expected form errors
        onView(withId(R.id.login_email_input)).check(matches(MatcherUtil.hasErrorText()));
        onView(withId(R.id.login_password_input)).check(matches(MatcherUtil.hasErrorText()));

    }

    @Test
    public void testBadCredentials(){
        // input some bad credentials into the form
        onView(withId((R.id.login_email_input)))
                .perform(typeText("bademail@email.com"));
        closeSoftKeyboard();

        onView(withId(R.id.login_password_input))
                .perform(typeText("NotTheRightPassword"));
        closeSoftKeyboard();


        // click the submit button
        onView(withId(R.id.email_sign_in_button)).perform(click());

        // check for the toast message
        onView(withText(R.string.bad_credentials)).
                inRoot(withDecorView(not(CoreMatchers.is(
                        loginActivityTest.getActivity().getWindow().getDecorView())
                ))).check(matches(isDisplayed()));
    }
    @Test
    public void testSuccessfulLogin(){
        // using the test account
        // typing in the credentials
        onView(withId((R.id.login_email_input)))
                .perform(typeText("test@mtu.edu"));
        closeSoftKeyboard();

        onView(withId(R.id.login_password_input))
                .perform(typeText("test"));
        closeSoftKeyboard();

        // click the submit button
        onView(withId(R.id.email_sign_in_button)).perform(click());

        intended(hasComponent(BoardsActivity.class.getName()));

    }

    @Test
    public void testSignupButton(){
        // click the signup text
        onView(withText(R.string.signup_message)).perform(click());

        // check for the signup activity
        intended(hasComponent(CreateUserActivity.class.getName()));
    }

    @After
    public void tearDown() throws Exception{
        Intents.release();
    }

}
