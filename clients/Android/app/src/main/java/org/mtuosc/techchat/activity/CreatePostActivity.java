package org.mtuosc.techchat.activity;

import android.content.Intent;
import android.support.v7.app.ActionBar;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.Toolbar;


import android.view.View;
import android.widget.AutoCompleteTextView;
import android.widget.MultiAutoCompleteTextView;
import android.widget.Toast;


import org.mtuosc.techchat.R;
import org.mtuosc.techchat.asynctasks.AsyncApiResponse;
import org.mtuosc.techchat.asynctasks.CreatePost;

public class CreatePostActivity extends BaseInternetActivity implements AsyncApiResponse<Boolean> {

    private AutoCompleteTextView titletextview;
    private MultiAutoCompleteTextView contenttextview;
    private int board_id;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.post_creation_activity);

        Toolbar toolbar = findViewById(R.id.toolbar2);
        toolbar.setTitle("Create a Post");
        setSupportActionBar(toolbar);
        ActionBar actionBar = getSupportActionBar();
        actionBar.setDisplayHomeAsUpEnabled(true);

        titletextview = findViewById(R.id.make_post_title_edit_text);
        contenttextview = findViewById(R.id.multiAutoCompleteTextView2);

        board_id = getIntent().getIntExtra("board_id", -1);




    }

    // handles the api call

    public void makePost(View view) {
        String title = titletextview.getText().toString();
        String content = contenttextview.getText().toString();
        if (title.isEmpty()) {
            titletextview.setError("title cannot be blank");
            return;
        }

        CreatePost apicall = new CreatePost(title, content, board_id, this);
        apicall.execute();

    }

    @Override
    public void taskCompleted(Boolean result) {
        if (!result) Toast.makeText(getApplicationContext(), "Could not create Post!", Toast.LENGTH_LONG).show();

        else {
            this.finish();
        }

    }
}
