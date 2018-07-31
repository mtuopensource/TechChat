package org.mtuosc.techchat.activity;


import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Toast;


import org.mtuosc.techchat.BoardsAdapter;
import org.mtuosc.techchat.R;

import org.mtuosc.techchat.RecyclerTouchListener;

import org.mtuosc.techchat.UserDataStorage;

import org.mtuosc.techchat.asynctasks.AsyncApiResponse;
import org.mtuosc.techchat.asynctasks.GetBoards;
import org.mtuosc.techchat.models.Board;


import java.util.ArrayList;


/**
 * This class will handle the boards view. The nav bar will contain some quick settings
 */
public class BoardsActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener , AsyncApiResponse{
    private RecyclerView boardRecyclerView;
    BoardsAdapter adapter;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.board_activity_base);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();
        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        // this gets data from the backend



        boardRecyclerView = findViewById(R.id.board_list);
        boardRecyclerView.setHasFixedSize(true);
        LinearLayoutManager llm = new LinearLayoutManager(this);
        llm.setOrientation(LinearLayoutManager.VERTICAL);
        boardRecyclerView.setLayoutManager(llm);

        adapter = new BoardsAdapter(new ArrayList<Board>());
        adapter.addBoardToAdapter(new Board("1", "Hello", "World"));
        boardRecyclerView.setAdapter(adapter);
        boardRecyclerView.addOnItemTouchListener(new RecyclerTouchListener(this, boardRecyclerView, new RecyclerTouchListener.ClickListener() {
            @Override
            public void onLongClick(View child, int childPosition) {
                onClick(child, childPosition);
            }

            @Override
            public void onClick(View child, int childPosition) {
                Board board = adapter.getBoardFrom(childPosition);
                Toast.makeText(BoardsActivity.this, board.getTitle(), Toast.LENGTH_SHORT).show();
            }
        }));


//        String cookie = getIntent().getExtras().getString("cookie");
//        GetBoards getBoards = new GetBoards(cookie, adapter, this);
//        getBoards.execute(10); //TODO default to 10: change this later



    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main2, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement


        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_logout){
            UserDataStorage storage = new UserDataStorage(getSharedPreferences("TechChat", Context.MODE_PRIVATE));
            storage.removeCurrentUserData();
            Intent goToLogin = new Intent(this, LoginActivity.class);
            startActivity(goToLogin);
            finish();
        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }


    @Override
    public void taskCompleted(Object result) {
        boardRecyclerView.setAdapter(adapter);
    }
}
