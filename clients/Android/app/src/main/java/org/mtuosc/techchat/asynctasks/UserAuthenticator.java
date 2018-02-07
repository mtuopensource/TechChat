package org.mtuosc.techchat.asynctasks;


import android.os.AsyncTask;

import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.mtuosc.techchat.ApiUrl;


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
        try {
            Response<String> response = webb.post(ApiUrl.LOGIN).param("email", email).param("password", password).
                    asString();
            if (response.getStatusCode() == 200)
                setAuthenticated(true);
            return isAuthenticated;
        }catch (Exception e){
            return false;
        }

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
            join(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
