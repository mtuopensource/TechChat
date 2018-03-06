package org.mtuosc.techchat.asynctasks;

import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Before;
import org.junit.Test;
import org.mtuosc.techchat.ApiUrl;
import org.mtuosc.techchat.BoardsAdapter;
import org.mtuosc.techchat.models.Board;

import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

import static org.junit.Assert.*;

/**
 * Created by ryan on 3/1/18.
 */
public class GetBoardsTest {

    @Test
    public void getTheBoards() {
        SignUpUserTaskTest signUpUser = new SignUpUserTaskTest();
        signUpUser.testUserCreation(); // creating a user
        Webb webb = Webb.create();
        webb.setBaseUri("http://ci.mtuopensource.club:8000");
        Response<String> object=  webb.post(ApiUrl.LOGIN).param("email", "test@mtu.edu")
                .param("password", "test").asString();
        assertTrue(object.getStatusCode() == 200);
        String cookie = object.getHeaderField("Set-Cookie");
        if (cookie != null){
            GetBoards getBoards = new GetBoards(cookie, new BoardsAdapter(new ArrayList<Board>()), new AsyncApiResponse<Response<JSONArray>>() {
                @Override
                public void taskCompleted(Response<JSONArray> result) {
                    if (!(result.getBody().length() > 0))
                        fail();
                }
            });
            getBoards.execute(5);
            try {
                Thread.sleep(400);
            } catch (InterruptedException e) {
                e.printStackTrace();
                fail();
            }
        }else
            fail("Cookie was not received");

    }
}