
import math

def block_nested_loop_join(outer_pages: int,inner_pages: int,buffers: int) -> int:
    total = outer_pages + (math.ceil(outer_pages/buffers) * inner_pages)
    return total

def index_nested_loop_join(outer_pages: int,outer_tuples:int, lookup_cost:float ) -> float:
    total = outer_pages + (outer_tuples * lookup_cost)
    return total

def hash_join(outer_pages: int, inner_pages: int) -> int:
    total = 3*(outer_pages + inner_pages)
    return total

def sort_merge_join(outer_pages: int, inner_pages:int, M:int) -> float:
    B = M-1
    sort_outer = 2*outer_pages*(1+math.log(B,outer_pages/B))
    sort_inner = 2*inner_pages*(1+math.log(B,inner_pages/B))
    total = sort_outer + sort_inner + outer_pages + inner_pages

    return total


def task_1(s_pages: int, r_pages: int, t_pages:int, K:int) -> None:
    
    total_a = block_nested_loop_join(s_pages,r_pages,K)
    print("a total: ", total_a)
    total_b = block_nested_loop_join(r_pages,s_pages,K)
    print("b total: ", total_b)
    total_c = block_nested_loop_join(r_pages,t_pages,K)
    print("c total: ", total_c)
    return


def task2(t_pages:int, t_tuples_pr_page:int, s_pages:int, K:int, M:int) -> None:
    #lookup cost s_Q
    lookup_cost = 0.25
    index_join_cost= index_nested_loop_join(t_pages,t_tuples_pr_page,lookup_cost)
    hash_join_cost = hash_join(t_pages,s_pages)
    sort_merge_cost = sort_merge_join(t_pages,s_pages,M)

    print("index nested loop cost: ", index_join_cost)
    print("hash join cost: ", hash_join_cost)
    print("sort-merge cost: ", sort_merge_cost)
    return






def main() -> None:
    #pages are represented as N^s for s pages and so on
    s_pages = 4500
    s_tuples_pr_page = 150
    r_pages = 1500
    r_tuples_pr_page = 80
    t_pages = 200
    t_tuples_pr_page = 250
   
    #available buffers: K = M-a
    #where a is how many you need to store data, see question
    M = 445
    K = M-2
    task_1(s_pages,r_pages,t_pages,K)
    task2(t_pages,t_tuples_pr_page,s_pages,K, M)
    return
    

    



if __name__ == "__main__":
    main()