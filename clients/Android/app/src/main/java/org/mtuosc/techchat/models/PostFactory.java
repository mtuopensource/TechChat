package org.mtuosc.techchat.models;

import org.json.JSONException;
import org.json.JSONObject;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class PostFactory {
    private static DateFormat dateFormat = new SimpleDateFormat("EEE MMM dd kk:mm:ss z yyyy",Locale.ENGLISH);

    public static Post createPostFromJSON(JSONObject json) throws JSONException {
        int id = json.getInt("id");
        String title = json.getString("title");
        String content = json.getString("description");
        int author = json.getInt("author");
        int board_id = json.getInt("board");
        String dateString = json.getString("timestamp");
        Date timestamp;
        try {
           timestamp = dateFormat.parse(dateString);
        } catch (ParseException e) {
            e.printStackTrace();
            timestamp = new Date(); // leave it blank so the app doesn't crash
        }
        return new Post(board_id, timestamp, title, content, author, id);
    }

}
