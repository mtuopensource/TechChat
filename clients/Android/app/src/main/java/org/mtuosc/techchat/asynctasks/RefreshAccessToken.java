package org.mtuosc.techchat.asynctasks;

import android.os.AsyncTask;
import android.util.Log;

import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONException;
import org.json.JSONObject;
import org.mtuosc.techchat.ApiUrl;
import org.mtuosc.techchat.UserData;

import java.util.logging.Logger;

public class RefreshAccessToken extends AsyncTask<Void, Void, Response<JSONObject>> {
    private String refreshToken;
    private Webb webb;
    private RefreshResponder responder;

    public RefreshAccessToken (RefreshResponder responder) {
        this.webb = Webb.create();
        this.responder = responder;
    }

    public void setRefreshToken(String refreshToken) {
        this.refreshToken = refreshToken;
    }

    @Override
    protected Response<JSONObject> doInBackground(Void... voids) {
        webb.setBaseUri(ApiUrl.SERVER_URL);
        return webb.post(ApiUrl.REFRESH).param("refresh", refreshToken).asJsonObject();
    }

    @Override
    protected void onPostExecute(Response<JSONObject> jsonObjectResponse) {
        try {
            String access = jsonObjectResponse.getBody().getString("access");
            responder.respondToRefresh(access);

        } catch (JSONException e) {
            e.printStackTrace();
            // If we are here that means we need a new refresh token as well
            UserData userData = UserData.getInstance();
            UserAuthenticator reAuthenticator = new UserAuthenticator(userData.getUsername(),
                                                                      userData.getPassword(),
            new AsyncApiResponse<Response<JSONObject>>() {
                        @Override
                        public void taskCompleted(Response<JSONObject> result) {
                            try {
                                responder.respondToRefresh(result.getBody().getString("access"));
                            } catch (JSONException ex) {
                                ex.printStackTrace();
                            }
                        }
                    });
            reAuthenticator.execute();
        }
    }
}
