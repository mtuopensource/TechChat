package org.mtuosc.techchat.asynctasks;

import android.os.AsyncTask;

import com.goebl.david.Response;
import com.goebl.david.Webb;

import org.json.JSONArray;
import org.json.JSONException;
import org.mtuosc.techchat.ApiUrl;
import org.mtuosc.techchat.BoardsAdapter;
import org.mtuosc.techchat.models.Board;
import org.mtuosc.techchat.models.BoardsFactory;


/**
 * Created by ryan on 2/23/18.
 * When calling execute, specify how many boards you want to load
 */

public class GetBoards extends AsyncTask<Integer, Double, Void> {
    Webb webb = Webb.create();
    private BoardsAdapter adapter;
    private String cookie;
    private AsyncApiResponse responser;


    public GetBoards(String cookie, BoardsAdapter adapter, AsyncApiResponse responser) {
        this.adapter = adapter;
        this.cookie = cookie;
        this.responser = responser;
    }

    @Override
    protected Void doInBackground(Integer... integers) {
        Response<JSONArray> boardsInJSON = getBoardsFromServer();
        addJSONBoardsToAdapter(integers[0], boardsInJSON.getBody());
        return null;
    }

    private void addJSONBoardsToAdapter(int numOfBoards, JSONArray body) {
        for (int i = 0; i < numOfBoards; i++) {
            try {
                Board board = BoardsFactory.createBoardFromJSON(body.getString(i));
                adapter.addBoardToAdapter(board);
            } catch (JSONException e) {
                e.printStackTrace();
                return; // isn't throwing a fuss
            }
        }
    }

    private Response<JSONArray> getBoardsFromServer(){
        webb.setBaseUri(ApiUrl.SERVER_URL);
        return webb.get(ApiUrl.GET_BOARDS).header("Cookie", "sessionid=" + cookie).asJsonArray();
    }

    @Override
    protected void onPostExecute(Void aVoid) {
        super.onPostExecute(aVoid);
        responser.taskCompleted(aVoid);
    }
}
