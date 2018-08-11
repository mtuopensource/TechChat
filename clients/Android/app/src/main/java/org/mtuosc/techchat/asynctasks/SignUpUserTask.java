package org.mtuosc.techchat.asynctasks;

import android.os.AsyncTask;

import android.util.Log;
import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONObject;
import org.mtuosc.techchat.ApiUrl;

/**
 * Created by ryan on 2/4/18.
 */

public class SignUpUserTask extends AsyncTask<Void, Void, Response<JSONObject>>{
    private Webb webb = Webb.create();
    private String email;
    private String password;
    private AsyncApiResponse<Response<JSONObject>> responder;

    public SignUpUserTask(String email, String password, AsyncApiResponse<Response<JSONObject>> responder) {
        webb.setBaseUri(ApiUrl.SERVER_URL);
        this.email = email;
        this.password = password;
        this.responder = responder;
    }

    @Override
    protected Response<JSONObject> doInBackground(Void... voids) {
        return webb.post(ApiUrl.SIGN_UP)
                .param("email", email).param("password",password).asJsonObject();
    }

    @Override
    protected void onPostExecute(Response<JSONObject> jsonObjectResponse) {
        String signupCookie = jsonObjectResponse.getHeaderField("Set-cookie");
        // TODO find a better solution
        if (signupCookie == null && jsonObjectResponse.getStatusCode() != 400){
            UserAuthenticator authenticator = new UserAuthenticator(this.email, this.password, responder);
            authenticator.execute();
            return;
        }
        responder.taskCompleted(jsonObjectResponse);
    }
}
