package org.mtuosc.techchat.models;

import android.os.Parcel;
import android.os.Parcelable;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

public class Post implements Parcelable {
    private int board_id;
    private Date timestamp;
    private String title;
    private String content;
    private int author;
    private int id;

    public Post(int board_id, Date timestamp, String title, String content, int author, int id) {
        this.board_id = board_id;
        this.timestamp = timestamp;
        this.title = title;
        this.content = content;
        this.author = author;
        this.id = id;
    }

    protected Post(Parcel in) {
        board_id = in.readInt();
        title = in.readString();
        content = in.readString();
        author = in.readInt();
        id = in.readInt();
        String dateString = in.readString();
        DateFormat dateFormat = new SimpleDateFormat("EEE MMM dd kk:mm:ss z yyyy", Locale.ENGLISH);
        try {
            timestamp = dateFormat.parse(dateString);
        } catch (ParseException e) {
            e.printStackTrace();
            timestamp = new Date();
        }

    }

    public static final Creator<Post> CREATOR = new Creator<Post>() {
        @Override
        public Post createFromParcel(Parcel in) {
            return new Post(in);
        }

        @Override
        public Post[] newArray(int size) {
            return new Post[size];
        }
    };

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel parcel, int i) {
        parcel.writeInt(board_id);
        parcel.writeString(title);
        parcel.writeString(content);
        parcel.writeInt(author);
        parcel.writeInt(id);
        parcel.writeString(timestamp.toString());
    }


    public Date getTimestamp() {
        return timestamp;
    }

    public String getTimestampString() {
        SimpleDateFormat sf = new SimpleDateFormat("dd/MM/YYYY", Locale.getDefault());
        return sf.format(timestamp);
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public int getAuthor() {
        return author;
    }

    public int getId() {
        return id;
    }
}
