package org.mtuosc.techchat;


import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Test;




import static org.junit.Assert.*;

/**
 * Created by ryan on 1/25/18.
 */
public class UserAuthenticatorTest {

    @Test
    public void testingLibrary(){
        Webb webb = Webb.create();
        webb.setBaseUri("http://141.219.197.116:8000");
       Response<String> object=  webb.post(ApiUrl.LOGIN.getName()).param("email", "ajwalhof@mtu.edu")
                .param("password", "test").asString();
       assertTrue(object.getStatusCode() == 200);

    }

    @Test
    public void simpleLogin(){
        UserAuthenticator authenticator = new UserAuthenticator("http://141.219.197.116:8000","ajwalhof@mtu.edu", "test");
        authenticator.start();
        try {
            authenticator.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
            fail();
        }
        System.out.print(authenticator.isAuthenticated());


    }

}