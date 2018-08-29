package org.mtuosc.techchat;

import android.content.Intent;
import android.support.test.filters.MediumTest;
import android.support.test.rule.ActivityTestRule;
import android.support.v7.widget.RecyclerView;

import com.goebl.david.Response;

import org.json.JSONObject;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;

import static org.junit.Assert.*;
import org.mtuosc.techchat.activity.BoardsActivity;


import org.mtuosc.techchat.activity.LoginActivity;
import org.mtuosc.techchat.asynctasks.AsyncApiResponse;
import org.mtuosc.techchat.asynctasks.UserAuthenticator;

@MediumTest
public class BoardActivityTest implements AsyncApiResponse<Response<JSONObject>>{

    private UserAuthenticator authenticator = new UserAuthenticator("test@mtu.edu",
                                                                 "test",
                                                                 this);
    private volatile String cookie = null;

    @Before
    public void getCookieData() {
        authenticator.execute();
        while (cookie == null){
        }
        Intent cookieIntent = new Intent();
        cookieIntent.putExtra("cookie", cookie);
        boardsActivityTest.launchActivity(cookieIntent);

    }

    @Rule
    public ActivityTestRule<BoardsActivity> boardsActivityTest =
            new ActivityTestRule<>(BoardsActivity.class, false, false);
    /**
     * This will be a fragile test,
     * as it will rely on a cookie to properly test the board retrieval
     */
    @Test
    public void testBoardRetrieval() {

        RecyclerView boardList = (RecyclerView) boardsActivityTest.getActivity().findViewById(R.id.board_list);
        assertTrue(boardList.getAdapter().getItemCount() > 0);
    }


    @Override
    public void taskCompleted(Response<JSONObject> result) {
        String cookieSession = result.getHeaderField("Set-Cookie"); //TODO parse out cookie
        cookie = LoginActivity.getCookieData(cookieSession);
    }
}
