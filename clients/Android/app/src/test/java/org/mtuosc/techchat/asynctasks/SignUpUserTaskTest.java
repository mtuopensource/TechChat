package org.mtuosc.techchat.asynctasks;

import com.goebl.david.Response;

import org.json.JSONObject;
import org.junit.Test;

import java.util.concurrent.ExecutionException;

import static org.junit.Assert.*;

/**
 * Created by ryan on 2/4/18.
 */
public class SignUpUserTaskTest {


    @Test
    public void testUserCreation(){

        SignUpUserTask task = new SignUpUserTask("tester@mtu.edu","test",
            new AsyncApiResponse<Response<JSONObject>>() {
                @Override
                public void taskCompleted(Response<JSONObject> result) {
                      if (result.getStatusCode() != 201)
                          fail();
                }
            });

            task.execute();
        try {
            Thread.sleep(200); // giving time for server to run
        } catch (InterruptedException e) {
            e.printStackTrace();
            fail();
        }
    }

}