package org.mtuosc.techchat.asynctasks;

import android.os.AsyncTask;
import android.util.JsonReader;

import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.mtuosc.techchat.ApiUrl;
import org.mtuosc.techchat.models.Post;
import org.mtuosc.techchat.models.PostAdapter;
import org.mtuosc.techchat.models.PostFactory;

public class GetPostsForBoard extends AsyncTask<Void, Void, Response<JSONArray>> {
    private Webb webb = Webb.create();
    private String access;
    private AsyncApiResponse<Response<JSONArray>> responder;
    private int board_id;
    private PostAdapter adapter;


    public GetPostsForBoard(int board_id, String access, PostAdapter adapter, AsyncApiResponse<Response<JSONArray>> responder) {
        this.board_id = board_id;
        this.access = access;
        this.responder = responder;
        webb.setBaseUri(ApiUrl.SERVER_URL);
        this.adapter = adapter;
    }


    @Override
    protected Response<JSONArray> doInBackground(Void... voids) {
        Response<JSONArray> response = getPostsFromServer();
        JSONArray postInJSON = response.getBody();
        for (int i = 0; i < postInJSON.length(); i++) {
            try {
                Post post = PostFactory.createPostFromJSON(postInJSON.getJSONObject(i));
                adapter.addPost(post);
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
        return response;
    }

    private Response<JSONArray> getPostsFromServer() {
        return webb.get(ApiUrl.BOARD_POSTS(board_id))
                .header("Authorization", "Bearer " + access)
                .asJsonArray();
    }

    @Override
    protected void onPostExecute(Response<JSONArray> aVoid) {
        super.onPostExecute(aVoid);
        responder.taskCompleted(aVoid);
    }
}
