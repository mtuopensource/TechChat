package org.mtuosc.techchat.activity;

import android.support.v7.app.ActionBar;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.Toolbar;

import org.mtuosc.techchat.R;

public class CreatePostActivity extends BaseInternetActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.post_creation_activity);

        Toolbar toolbar = findViewById(R.id.toolbar2);
        toolbar.setTitle("Create a Post");
        setSupportActionBar(toolbar);
        ActionBar actionBar = getSupportActionBar();
        actionBar.setDisplayHomeAsUpEnabled(true);


    }
}
