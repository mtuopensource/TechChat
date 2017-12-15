package org.mtuosc.techchat.models;
/**
 * Created by ryan on 11/28/17.
 */
import org.json.*;


public class BoardsFactory {

    public static Board createBoardFromJSON(String json) throws JSONException {
        JSONObject jsonObject = new JSONObject(json);
        String id = jsonObject.getString("id");
        String title = jsonObject.getString("title");
        String description = jsonObject.getString("description");
        return new Board(id, title, description);
    }
}
