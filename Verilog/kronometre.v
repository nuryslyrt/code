module KRONOMETRE (CLOCK_50, KEY, HEX7,HEX6,HEX5,HEX4,HEX3,HEX2, HEX1);
	/******************************************************************/
	/****      PORT TANIMLAMALARI                                  ****/
	/******************************************************************/
	input CLOCK_50;
	input [3:0] KEY;
	output [0:6] HEX7,HEX6,HEX5,HEX4,HEX3,HEX2, HEX1;
	
	/******************************************************************/
	/****      WIRE TANIMLAMALARI,,,                                  ****/
	/******************************************************************/
	wire 		bir_saniye_enable;
	wire [3:0]	one_wires, ten_wires, hundred_wires, monlar_wires, sonlar_wires, sbirler_wires, mbirler_wires;
	wire 		roll_ones, roll_tens, roll_mones, roll_sones, roll_yuzler,roll_stens;
	
	/******************************************************************/
	/****      UYGULAMA                                            ****/
	/******************************************************************/
	//assign stop = (KEY[1])? ~stop:stop;
	modulo_counter yeni_clock(.clock(CLOCK_50),
					.reset_n(KEY[0]),
					.enable(1'B1),
					.basa_sar(bir_saniye_enable));
		defparam yeni_clock.n = 27;
		defparam yeni_clock.k = 50000;
	
	// Uc Basamak
	modulo_counter birler( .clock(CLOCK_50),
				.reset_n(KEY[0]),
				.enable(bir_saniye_enable),
				.Q(birler_wires),
				.basa_sar(roll_ones));
		defparam birler.n = 4;
		defparam birler.k = 10;
		
	modulo_counter onlar( .clock(CLOCK_50),
				.reset_n(KEY[0]),
				.enable(bir_saniye_enable & roll_ones),
				.Q(onlar_wires),
				.basa_sar(roll_tens));
		defparam onlar.n = 4;
		defparam onlar.k = 10;
		
	modulo_counter yuzler( .clock(CLOCK_50),
				.reset_n(KEY[0]),
				.enable(bir_saniye_enable & roll_ones & roll_tens),
				.Q(yuzler_wires),
				.basa_sar(roll_yuzler));
		defparam yuzler.n = 4;
		defparam yuzler.k = 10;
		
	modulo_counter sbirler( .clock(CLOCK_50),
				.reset_n(KEY[1]),
				.enable(bir_saniye_enable & roll_ones & roll_tens&roll_yuzler),
				.Q(sbirler_wires),
				.basa_sar(roll_sones));
		defparam sbirler.n = 4;
		defparam sbirler.k = 10;
		
	modulo_counter sonlar( .clock(CLOCK_50),
				.reset_n(KEY[1]),
				.enable(bir_saniye_enable & roll_ones & roll_tens&roll_yuzler&roll_sones),
				.Q(sonlar_wires),
				.basa_sar(roll_stens));
		defparam sonlar.n = 4;
		defparam sonlar.k = 6;
	
	modulo_counter mbirler( .clock(CLOCK_50),
				.reset_n(KEY[2]),
				.enable(bir_saniye_enable & roll_ones & roll_tens&roll_yuzler&roll_sones&roll_stens),
				.Q(mbirler_wires),
				.basa_sar(roll_mones));
		defparam mbirler.n = 4;
		defparam mbirler.k = 10;
		
	modulo_counter monlar( .clock(CLOCK_50),
				.reset_n(KEY[2]),
				.enable(bir_saniye_enable & roll_ones & roll_tens&roll_yuzler&roll_sones&roll_stens&roll_mones),
				.Q(monlar_wires),
				.basa_sar());
		defparam monlar.n = 4;
		defparam monlar.k = 6;
		
	
	
	bcd7seg digit7 (monlar_wires, HEX7);
	bcd7seg digit6 (mbirler_wires, HEX6);
	bcd7seg digit5 (sonlar_wires, HEX5);
	bcd7seg digit4 (sbirler_wires, HEX4);
	bcd7seg digit3 (yuzler_wires, HEX3);
	bcd7seg digit2 (onlar_wires, HEX2);
	bcd7seg digit1	(birler_wires, HEX1);
	
endmodule

module bcd7seg(bcd, display);
//bcd7seg
/****      PORT TANIMLAMALARI                                   ****/
	/******************************************************************/
	input [3:0] bcd;
	output reg [0:6] display;
	
	/******************************************************************/
	/****      UYGULAMA                                            ****/
	/******************************************************************/
	/*
	 *       0  
	 *      ---  
	 *     |   |
	 *    5|   |1
	 *     | 6 |
	 *      ---  
	 *     |   |
	 *    4|   |2
	 *     |   |
	 *      ---  
	 *       3  
	 */
	always @ (bcd)
		case (bcd)
			4'h0: display = 7'b0000001;
			4'h1: display = 7'b1001111;
			4'h2: display = 7'b0010010;
			4'h3: display = 7'b0000110;
			4'h4: display = 7'b1001100;
			4'h5: display = 7'b0100100;
			4'h6: display = 7'b0100000;
			4'h7: display = 7'b0001111;
			4'h8: display = 7'b0000000;
			4'h9: display = 7'b0000100;
			default: display = 7'b1111111;
		endcase
endmodule
/**************************************************************************************************/



//modulo_counter
module modulo_counter(clock, reset_n, enable, basa_sar,Q);
	/******************************************************************/
	/****      PARAMETRE TANIMLAMALARI                             ****/
	/******************************************************************/
	parameter 		n = 27;       // Bit uzunlugu
	parameter 		k = 50000; // Durma noktası sn için 50000
	
	/******************************************************************/
	/****      PORT TANIMLAMALARI                                  ****/
	/******************************************************************/
	input 			clock, reset_n, enable;
	output			basa_sar;
        output 	[n-1:0]	Q;
	reg 	[n-1:0]	Q;

	/******************************************************************/
	/****      UYGULAMA                                            ****/
	/******************************************************************/
	always @ (posedge clock or negedge reset_n)
		if (~reset_n)
			Q <= 'd0;
		else if (enable)
		begin
			if (Q == k-1) // Eger durma noktasina geldiyse sifirla
				Q <= 'd0;
			else
				Q <= Q + 1'b1;
		end
				
	assign basa_sar = (Q == k-1);	
endmodule
/********************************************************************************************************/
