
import multiprocessing as mp
import subprocess

def run_program(program_name):
  subprocess.run(["python3", program_name])

if __name__ == '__main__':
    num_cpu_cores = mp.cpu_count()
  # Create a pool of worker processes
    with mp.Pool(num_cpu_cores) as pool:
    # Start all of the programs concurrently
        pool.apply_async(run_program, ("/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program1.py",))
        pool.apply_async(run_program, ("/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program2.py",))
        pool.apply_async(run_program, ("/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program3.py",))
        pool.apply_async(run_program, ("/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program4.py",))

    # Wait for all of the programs to finish
        pool.close()
        pool.join()
