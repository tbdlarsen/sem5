
import math



def main():
    N_S = 4500
    N_R = 1500
    N_T = 200
    K = 443

    total_a = N_S + (math.ceil(N_S/443) * N_R)
    total_b = N_R + (math.ceil(N_R/443) * N_S)
    total_c = N_R + (math.ceil(N_R/443) * N_T)

    print(total_c)



if __name__ == "__main__":
    main()