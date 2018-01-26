package org.mtuosc.techchat;

/**
 * Created by ryan on 11/28/17.
 * This will specify the urls for the api back end.
 * This will allow the whole application to easily change url patterns
 */

public enum ApiUrl {
    GET_BOARDS("/api/boards"),
    LOGIN("/api/Users/login");

    private String name;
    ApiUrl(String string) {
    }
    public String getName(){
        return name;
    }

}
