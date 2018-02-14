package org.mtuosc.techchat.asynctasks;

import android.os.AsyncTask;

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
    private AsyncApiResponse responder;

    public SignUpUserTask(String serverIP, String email, String password, AsyncApiResponse responder) {
        webb.setBaseUri(serverIP);
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
        super.onPostExecute(jsonObjectResponse);
        responder.taskCompleted(jsonObjectResponse);
    }
}
