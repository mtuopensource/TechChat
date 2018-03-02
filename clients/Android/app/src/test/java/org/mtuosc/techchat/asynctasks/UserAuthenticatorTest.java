package org.mtuosc.techchat.asynctasks;


import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONObject;
import org.junit.Test;
import org.mtuosc.techchat.ApiUrl;
import org.mtuosc.techchat.asynctasks.UserAuthenticator;


import static org.junit.Assert.*;

/**
 * Created by ryan on 1/25/18.
 */
public class UserAuthenticatorTest implements AsyncApiResponse<Response<JSONObject>> {

    @Test
    public void testingLibrary(){
        Webb webb = Webb.create();
        webb.setBaseUri("http://ci.mtuopensource.club:8000");
       Response<String> object=  webb.post(ApiUrl.LOGIN).param("email", "test@mtu.edu")
                .param("password", "test").asString();
       assertTrue(object.getStatusCode() == 200);

    }

    @Test
    public void simpleLogin(){
        UserAuthenticator authenticator = new UserAuthenticator("test@mtu.edu", "test", this);
        authenticator.execute();

    }

    @Override
    public void taskCompleted(Response<JSONObject> result) {
        if (result.getStatusCode() != 200)
            fail("user not logged in");
    }
}