package org.mtuosc.techchat.models;

import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import org.mtuosc.techchat.R;

import java.util.List;

/**
 * Created by ryan on 11/28/17.
 */

public class BoardsAdapter extends RecyclerView.Adapter<BoardsAdapter.BoardViewHolder> {
    private List<Board> boardList;

    public class BoardViewHolder extends RecyclerView.ViewHolder{
        public TextView boardTitle;
        public TextView boardDesc;

        public BoardViewHolder(View itemView) {
            super(itemView);
            boardTitle = itemView.findViewById(R.id.board_row_title);
            boardDesc = itemView.findViewById(R.id.board_row_description);

        }
    }


    public BoardsAdapter(List<Board> boards) {
        boardList = boards;

    }

    @Override
    public BoardViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.board_row_layout, parent, false);
        return new BoardViewHolder(view);
    }

    @Override
    public void onBindViewHolder(BoardViewHolder holder, int position) {
        Board board = boardList.get(position);
        holder.boardDesc.setText(board.getDescription());
        holder.boardTitle.setText(board.getTitle());
    }

    @Override
    public int getItemCount() {
        return boardList.size();
    }

    public Board getBoardFrom(int position){
        return boardList.get(position);
    }

    public void addBoardToAdapter(Board board){
        boardList.add(board);
    }




}
