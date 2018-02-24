package org.mtuosc.techchat.asynctasks;


import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.junit.Test;
import org.mtuosc.techchat.ApiUrl;
import org.mtuosc.techchat.asynctasks.UserAuthenticator;


import static org.junit.Assert.*;

/**
 * Created by ryan on 1/25/18.
 */
public class UserAuthenticatorTest {

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
        UserAuthenticator authenticator = new UserAuthenticator("http://ci.mtuopensource.club:8000","test@mtu.edu", "test");
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