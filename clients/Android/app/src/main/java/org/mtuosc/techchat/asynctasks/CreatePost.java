package org.mtuosc.techchat.asynctasks;

import android.os.AsyncTask;

import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONObject;
import org.mtuosc.techchat.ApiUrl;
import org.mtuosc.techchat.UserData;

public class CreatePost extends AsyncTask<Void, Void, Boolean> {
    private String title, content;
    private int board_id;
    private Webb webb = Webb.create();
    private AsyncApiResponse<Boolean> responder;

    public CreatePost(String title, String content, int board_id, AsyncApiResponse<Boolean> responder) {
        this.board_id = board_id;
        this.title = title;
        this.content = content;
        webb.setBaseUri(ApiUrl.SERVER_URL);
        this.responder = responder;

    }

    @Override
    protected Boolean doInBackground(Void... voids) {
        Response<JSONObject> response = webb.post(ApiUrl.CREATE_POSTS).param("board", this.board_id)
                .param("title", title).param("description", content)
                .header("Authorization", "Bearer " + UserData.getInstance().getAccessToken()).asJsonObject();

        return response.getStatusCode() == 201;
    }


    @Override
    protected void onPostExecute(Boolean aBoolean) {
        super.onPostExecute(aBoolean);
        this.responder.taskCompleted(aBoolean);
    }
}
