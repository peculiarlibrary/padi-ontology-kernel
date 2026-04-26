import subprocess
import os

class Executor:
    """The PADI Bureau Executor: Translates commands into system processes."""
    
    def spawn_agent(self, agent_name, script_path):
        """Spawns a junior agent as an autonomous sub-process."""
        print(f"[EXECUTOR] Spawning agent: {agent_name}...")
        
        # Ensures the agent operates within the sovereign workspace
        cmd = ["python", script_path]
        
        try:
            # We use Popen for non-blocking, autonomous execution
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return process.pid
        except Exception as e:
            print(f"[ERROR] Executor failed to spawn {agent_name}: {e}")
            return None

    def check_status(self, pid):
        """Verifies if an agent is still alive and reporting."""
        return os.kill(pid, 0) == None
