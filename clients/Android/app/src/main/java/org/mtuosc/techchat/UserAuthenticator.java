package org.mtuosc.techchat;


import android.os.AsyncTask;

import com.goebl.david.Response;
import com.goebl.david.Webb;




/**
 * Created by ryan on 12/15/17.
 */

public class UserAuthenticator extends Thread {
    private String email, password;
    private boolean isAuthenticated = false;
    private Webb webb = Webb.create();


    public UserAuthenticator(String serverIp, String email, String password) {
        webb.setBaseUri(serverIp);
        this.email = email;
        this.password = password;
    }

    private boolean logUserIn(String email, String password){

       Response<String> response = webb.post(ApiUrl.LOGIN.getName()).param("email", email).param("password", password).
               asString();
       if (response.getStatusCode() == 200)
           setAuthenticated(true);
       else
           setAuthenticated(false);
       return isAuthenticated;

    }

    private void setAuthenticated(boolean authenticated) {
        isAuthenticated = authenticated;
    }

    public boolean isAuthenticated(){
        return isAuthenticated;
    }

    @Override
    public void run() {
        super.run();
        logUserIn(email, password);
    }

    public void startLogin(){
        start();
        try {
            join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
