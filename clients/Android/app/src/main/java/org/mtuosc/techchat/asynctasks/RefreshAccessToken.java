package org.mtuosc.techchat.asynctasks;

import android.os.AsyncTask;

import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONException;
import org.json.JSONObject;
import org.mtuosc.techchat.ApiUrl;

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
        }
    }
}
