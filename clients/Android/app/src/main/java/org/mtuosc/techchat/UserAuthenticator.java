package org.mtuosc.techchat;

import android.os.AsyncTask;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;
import com.loopj.android.http.RequestParams;


import java.util.HashMap;

import cz.msebera.android.httpclient.Header;

/**
 * Created by ryan on 12/15/17.
 */

public class UserAuthenticator {
    private String serverIp;
    private boolean isAuthenticated = false;

    public UserAuthenticator(String serverIp) {
        this.serverIp = serverIp;
    }

    public boolean logUserIn(String email, String password){
        RequestParams loginParams = createRequestParams(email, password);
        AsyncHttpClient client = new AsyncHttpClient();
        client.get("http://" + serverIp + ApiUrl.LOGIN.getName(), loginParams, new AsyncHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers, byte[] responseBody) {
                setAuthenticated(true);
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, byte[] responseBody, Throwable error) {
                if(statusCode == 401) // user enter invalid credentials
                    setAuthenticated(false);
            }
        });
        return isAuthenticated();
    }

    private RequestParams createRequestParams(String email, String password){
        HashMap<String, String> paramData = new HashMap<>();
        paramData.put("email", email);
        paramData.put("password", password);
        return  new RequestParams(paramData);
    }

    private boolean isAuthenticated() {
        return isAuthenticated;
    }

    private void setAuthenticated(boolean authenticated) {
        isAuthenticated = authenticated;
    }

}
