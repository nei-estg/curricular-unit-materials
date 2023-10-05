package battleShip;

import java.util.Random;
import java.util.Scanner;

public class BattleShip 
{
    private static Scanner input;

    public static void main(String[] args) 
    {
        int[][] board = new int[5][5];
        int[][] ships = new int[3][2];
        int[] shot = new int[2];
        int attempts=0, shotHit=0;
        
        initBoard(board);
        initShips(ships);
        
        input = new Scanner(System.in);
        
        System.out.println();
        
        do{
            showBoard(board);
            shoot(shot);
            
            attempts++;
            
            if(hit(shot,ships))
            {
                hint(shot,ships,attempts);
                shotHit++;
            }                
            else
                hint(shot,ships,attempts);
            
            changeboard(shot,ships,board);
            

        } while(shotHit!=3);
        
        System.out.println("\n\n\nFim do Simulador Batalha Naval! Acertaste nos 3 barcos em "+attempts+" tentativas");
        
        showBoard(board);
        
        input.close();
    }
    
    public static void initBoard(int[][] board)
    {
        for(int row=0 ; row < 5 ; row++ )
        {
            for(int column=0 ; column < 5 ; column++ )
            {
                board[row][column]=-1;
            }
        }
    }
    
    public static void showBoard(int[][] board){
        System.out.println("\t1 \t2 \t3 \t4 \t5");
        System.out.println();
        
        for(int row=0 ; row < 5 ; row++ )
        {
            System.out.print((row+1)+"");
            for(int column=0 ; column < 5 ; column++ )
            {
                if(board[row][column]==-1)
                {
                    System.out.print("\t"+"~");
                } 
                else if(board[row][column]==0) 
                {
                    System.out.print("\t"+"*");
                }
                else if(board[row][column]==1)
                {
                    System.out.print("\t"+"X");
                }
                
            }
            System.out.println();
        }

    }

    public static void initShips(int[][] ships)
    {
        Random random = new Random();
        
        for(int ship=0 ; ship < 3 ; ship++)
        {
            ships[ship][0]=random.nextInt(5);
            ships[ship][1]=random.nextInt(5);
            
            //let's check if that shot was already tried 
            //if it was, just finish the do...while when a new pair was randomly selected
            for(int last=0 ; last < ship ; last++)
            {
                if((ships[ship][0] == ships[last][0])&&(ships[ship][1] == ships[last][1]))
                    do
                    {
                    	ships[ship][0]=random.nextInt(5);
                        ships[ship][1]=random.nextInt(5);
                    } while( (ships[ship][0] == ships[last][0])&&(ships[ship][1] == ships[last][1]) );
            }
            
        }
    }

    public static void shoot(int[] shot)
    {        
        System.out.print("Linha: ");
        shot[0] = input.nextInt();
        shot[0]--;
        
        System.out.print("Coluna: ");
        shot[1] = input.nextInt();
        shot[1]--;        
    }
    
    public static boolean hit(int[] shot, int[][] ships)
    {
        for(int ship=0 ; ship<ships.length ; ship++)
        {
            if( shot[0]==ships[ship][0] && shot[1]==ships[ship][1])
            {
                System.out.printf("Acertaste num barco na posição (%d,%d)\n",shot[0]+1,shot[1]+1);
                return true;
            }
        }
        return false;
    }

    public static void hint(int[] shot, int[][] ships, int attempt)
    {
        int row=0, column=0;
        
        for(int line=0 ; line < ships.length ; line++)
        {
            if(ships[line][0]==shot[0])
                row++;
            if(ships[line][1]==shot[1])
                column++;
        }
        
        System.out.printf("\nDica %d: \nLinha %d -> %d barco(s)\n" + "Coluna %d -> %d barco(s)\n",attempt,shot[0]+1,row,shot[1]+1,column);
    }

    public static void changeboard(int[] shot, int[][] ships, int[][] board)
    {
        if(hit(shot,ships))
            board[shot[0]][shot[1]]=1;
        else
            board[shot[0]][shot[1]]=0;
    }
}
