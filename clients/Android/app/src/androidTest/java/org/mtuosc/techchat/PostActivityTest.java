package org.mtuosc.techchat;


import android.content.Intent;
import android.support.test.filters.MediumTest;
import android.support.test.rule.ActivityTestRule;
import android.support.v7.widget.RecyclerView;

import com.goebl.david.Response;

import org.json.JSONException;
import org.json.JSONObject;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.mtuosc.techchat.activity.PostActivity;
import org.mtuosc.techchat.asynctasks.AsyncApiResponse;
import org.mtuosc.techchat.asynctasks.UserAuthenticator;

import static junit.framework.Assert.assertTrue;
import static junit.framework.TestCase.fail;

@MediumTest
public class PostActivityTest implements AsyncApiResponse<Response<JSONObject>> {

    private UserAuthenticator authenticator = new UserAuthenticator("test@mtu.edu",
                                                            "test",
                                                            this);

    private volatile String accessToken = null;


    @Before
    public void getCookieData() {
        authenticator.execute();
        while(accessToken == null);
        UserData.getInstance().setAccessToken(accessToken);
        // we should always have a board with id 1
        Intent intentForTest = new Intent();
        intentForTest.putExtra("board_id", "1");
        postActivityTest.launchActivity(intentForTest);
    }

    @Rule
    public ActivityTestRule<PostActivity> postActivityTest =
            new ActivityTestRule<>(PostActivity.class, false, false);

    @Test
    public void testPostRetrieval() {
        RecyclerView postList = postActivityTest.getActivity().findViewById(R.id.post_list);
        assertTrue(postList.getAdapter().getItemCount() > 0);
    }


    @Override
    public void taskCompleted(Response<JSONObject> result) {
        try {
            accessToken = result.getBody().getString("access");
        } catch (JSONException e) {
            e.printStackTrace();
            fail("Could not parse the access token!");
        }
    }
}
