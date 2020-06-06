package org.mtuosc.techchat;

import org.mtuosc.techchat.asynctasks.AsyncApiResponse;


/**
 * Holds any relevant data regarding the user
 */
public class UserData implements AsyncApiResponse<String> {
    private String refreshToken;
    private String accessToken;
    private String username;
    private String password;
    private long lastAccessTokenRefresh = Long.MIN_VALUE; // time the access token was generated
    private static UserData data = new UserData();
    private static long ACCESS_TOKEN_LIFETIME = 1200000; // 2 minutes in milliseconds

    private UserData() {

    }

    public static UserData getInstance() { return data; }

    public boolean userExists(){
        return refreshToken.length() > 0;
    }

    public String getRefreshToken() { return this.refreshToken; }

    public void setRefreshToken(String refreshToken) {
        this.refreshToken = refreshToken;
    }

    public String getAccessToken() {
        return accessToken;
    }

    public boolean isAccessTokenValid() {
        long currentTime = System.currentTimeMillis();
        return (lastAccessTokenRefresh > 0 &&
                (currentTime - lastAccessTokenRefresh) <= ACCESS_TOKEN_LIFETIME );
    }

    public void setAccessToken(String accessToken) {
        this.lastAccessTokenRefresh = System.currentTimeMillis();
        this.accessToken = accessToken;
    }

    @Override
    public void taskCompleted(String result) {
        this.accessToken = result;
        this.lastAccessTokenRefresh = System.currentTimeMillis();
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
