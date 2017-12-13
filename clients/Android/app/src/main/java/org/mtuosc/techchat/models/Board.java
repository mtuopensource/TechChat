package org.mtuosc.techchat.models;

/**
 * Created by ryan on 11/28/17.
 * Model version of boards
 */

public class Board {
    private String id;
    private String title;
    private String description;

    public Board(String id, String title, String description) {
        this.id = id;
        this.title = title;
        this.description = description;
    }

    public String getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }
}
