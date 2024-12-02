
import os
import torch
import torch.distributed as dist
import torch.multiprocessing as mp

"""Blocking point-to-point communication."""

def p2p(rank, size):
    tensor = torch.randn(1, 2, 3)
    if rank == 0:
        tensor += 1
        # Send the tensor to process 1
        dist.send(tensor=tensor, dst=1)
    else:
        # Receive tensor from process 0
        dist.recv(tensor=tensor, src=0)
    print('Rank ', rank, ' has data ', tensor)


"""Non-blocking point-to-point communication."""

def p2p_(rank, size):
    tensor = torch.randn(1, 2, 3)
    req = None
    if rank == 0:
        tensor += 1
        # Send the tensor to process 1
        req = dist.isend(tensor=tensor, dst=1)
        print('Rank 0 started sending')
    else:
        # Receive tensor from process 0
        req = dist.irecv(tensor=tensor, src=0)
        print('Rank 1 started receiving')
    req.wait()
    print('Rank ', rank, ' has data ', tensor)


""" All-Reduce example."""
def all_reduce(rank, size):
    """ Simple collective communication. """
    group = dist.new_group([0, 1])
    # tensor = torch.ones(1)
    tensor = torch.randn(1, 2, 3)
    print('--------------Rank ', rank, ' src data ', tensor)
    dist.all_reduce(tensor, op=dist.ReduceOp.PREMUL_SUM, group=group)
    print('++++++++++++++Rank ', rank, ' dst data ', tensor)


""" Reduce example."""
def reduce(rank, size):
    """ Simple collective communication. """
    group = dist.new_group([0, 1])
    tensor = torch.randn(1, 2, 3)
    print('--------------Rank ', rank, ' src data ', tensor)
    dist.reduce(tensor, dst=0, op=dist.ReduceOp.SUM, group=group)
    print('++++++++++++++Rank ', rank, ' dst data ', tensor)

""" Broadcast example."""
def broadcast(rank, size):
    """ Simple collective communication. """
    group = dist.new_group([0, 1])
    tensor = torch.randn(1, 2, 3)
    print('--------------Rank ', rank, ' src data ', tensor)
    dist.broadcast(tensor, src=0, group=group)
    print('++++++++++++++Rank ', rank, ' dst data ', tensor)

""" Scatter example."""
def scatter(rank, size):
    """ Simple collective communication. """
    group = dist.new_group([0, 1])
    if rank == 0:
        # 进程0准备要分散的张量
        tensor = torch.tensor([[1.0, 2.0, 3.0],
                                [4.0, 5.0, 6.0]])  # 2x3的张量
        scatter_list = [tensor[i].unsqueeze(0) for i in range(tensor.size(0))]  # 创建散列列表
    else:
        scatter_list = None  # 其他进程不需要任何数据
    print('--------------Rank ', rank, ' src data ', scatter_list)
    # 每个进程都准备一个空张量来接收数据
    recv_tensor = torch.empty(1,3)

    dist.scatter(recv_tensor, scatter_list, src=0, group=group)
    print('++++++++++++++Rank ', rank, ' dst data ', recv_tensor)

""" Gather example."""
def gather(rank, size):
    """ Simple collective communication. """
    group = dist.new_group([0, 1])
    tensor = torch.randn(1, 2, 3)
    print('--------------Rank ', rank, ' src data ', tensor)
    # 进程0将接收所有数据
    gather_list = None
    if rank == 0:
        gather_list = [torch.empty_like(tensor) for _ in range(size)]  # 为收集的数据分配空间

    dist.gather(tensor, gather_list=gather_list, dst=0, group=group)
    print('++++++++++++++Rank ', rank, ' dst data ', gather_list)

""" All-Gather example."""
def all_gather(rank, size):
    """ Simple collective communication. """
    group = dist.new_group([0, 1])
    tensor = torch.randn(1, 2, 3)
    print('--------------Rank ', rank, ' src data ', tensor)
    # 进程0将接收所有数据
    gather_list = [torch.empty_like(tensor) for _ in range(size)]  # 为收集的数据分配空间
        
    # 使用 all_gather 操作收集所有进程的张量
    dist.all_gather(gather_list, tensor, group=group)
    # dist.all_gather(tensor_list, tensor, group)
    print('++++++++++++++Rank ', rank, ' dst data ', gather_list)


def init_process(rank, size, fn, backend='gloo'):
    """ Initialize the distributed environment. """
    os.environ['MASTER_ADDR'] = '127.0.0.1'
    os.environ['MASTER_PORT'] = '29500'
    dist.init_process_group(backend, rank=rank, world_size=size)
    fn(rank, size)


if __name__ == "__main__":
    world_size = 2
    processes = []
    mp.set_start_method("spawn")
    for rank in range(world_size):
        p = mp.Process(target=init_process, args=(rank, world_size, all_reduce))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
