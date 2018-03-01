package org.mtuosc.techchat.asynctasks;


import android.os.AsyncTask;

import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONArray;
import org.json.JSONObject;
import org.mtuosc.techchat.ApiUrl;


/**
 * Created by ryan on 12/15/17.
 */

public class UserAuthenticator extends AsyncTask<Void, Void, Response<JSONObject>> {
    private String email, password;
    private Webb webb = Webb.create();
    private AsyncApiResponse<Response<JSONObject>> responder;


    public UserAuthenticator(String email, String password, AsyncApiResponse<Response<JSONObject>> responder) {
        webb.setBaseUri(ApiUrl.SERVER_URL);
        this.email = email;
        this.password = password;
        this.responder = responder;
    }


    @Override
    protected Response<JSONObject> doInBackground(Void... voids) {
        return webb.post(ApiUrl.LOGIN).param("email", email).param("password", password).asJsonObject();
    }

    @Override
    protected void onPostExecute(Response<JSONObject> jsonObjectResponse) {
        responder.taskCompleted(jsonObjectResponse);
    }
}
