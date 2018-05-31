package org.mtuosc.techchat;


/**
 * Holds any relevant data regarding the user
 */
public class UserData {
    private String cookie;

    public UserData(String cookie) {
        this.cookie = cookie;
    }

    public boolean userExists(){
        return cookie.length() > 0;
    }


    public String getCookie(){
        return this.cookie;
    }

}
