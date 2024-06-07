# node.py
import subprocess
import numpy as np

class Node:
    def __init__(self, prefix, index, ks, refs):
        self.prefx = prefix
        self.index = index
        self.ks = ks
        self.refs = refs

    def get_avs_and_grads(self):
        data_file = self.prefix+'_'+str(self.index)+'.dat'
        # Open the file and read the first line to determine the number of columns
        with open(data_file, 'r') as file:
            line = file.readline()
            num_cols = len(line.split())
        data = np.loadtxt(data_file, usecols=range(1,num_cols))
        self.avs = np.mean(data,axis=0)
        self.grads = self.ks*(self.avs-self.refs)

    def run_node(self):
        # Define file names
        top_file = f"{self.prefix}.prmtop"
        dat_file = f"{self.prefix}_{self.index}.dat"
        rst_file = f"{self.prefix}_{self.index}.rst"
        mdin_file = f"{self.prefix}_{self.index}.mdin"
        mdout_file = f"{self.prefix}_{self.index}.mdout"
        inf_file = f"{self.prefix}_{self.index}.inf"
        nc_file = f"{self.prefix}_{self.index}.nc"
        rst7_file = f"{self.prefix}_{self.index}.rst7"
        old_rst7_file = f"{self.prefix}_old_{self.index}.rst7"
        run_dir=f"temp_{self.index}"

        # A temporary directory is created to run the node simulation
        # We move there and copy the input files

        subprocess.run(["mkdir","-p", run_dir])
        subprocess.run(["cd", run_dir])
        subprocess.run(["cp", inputs_dir, "/*", "."])

        # Edit templates
        # The mdin file has the names for rst and dat files but with the string
        # "index" instead of the actual index value

        replace_placeholders(mdin_file, {"index": str(self.index)})

        amber_run_command = [
        mdexe, "-O", 
        "-i", mdin_file,
        "-p", top_file,
        "-c", old_rst7_file,
        "-r", rst7_file,
        "-x", nc_file,
        "-inf", inf_file,
        "-o", mdout_file
        ]

        subprocess.run(command)


    
    def replace_placeholders(template_path, replacements, output_path):
        # Read the template file
        with open(template_path, 'r') as file:
            content = file.read()

        # Replace all placeholders using the dictionary
        for placeholder, replacement in replacements.items():
            pattern = r"\{" + re.escape(placeholder) + r"\}"
            content = re.sub(pattern, replacement, content)

        # Write the modified content overwriting the old one
        with open(template_path, 'w') as file:
            file.write(content)

# template = "Job running on {node}, using {cpu} CPUs."
# replacements = {"node": "node01", "cpu": "16"}

# new_script = replace_placeholders(template, replacements)
# print(new_script)


    def update_structure(self):
        rst_file = f"node_{self.index}.rst"
        # Implement the method to update the structure file
