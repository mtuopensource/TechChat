package org.mtuosc.techchat;

/**
 * Created by ryan on 11/28/17.
 * This will specify the urls for the api back end.
 * This will allow the whole application to easily change url patterns
 */

public class ApiUrl {
    public static final String SERVER_HOSTNAME = "open-source-at-mtu-tech-chat.herokuapp.com";
    public static final String SERVER_URL = "https://open-source-at-mtu-tech-chat.herokuapp.com";
    public static final String GET_BOARDS = "/api/boards/";
    public static final String LOGIN = "/api/token/";
    public static final String REFRESH = "/api/token/refresh/";
    public static final String VERIFY = "/api/token/verify/";
    public static final String SIGN_UP = "/api/users/";


}
