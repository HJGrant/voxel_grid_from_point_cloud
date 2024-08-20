import open3d as o3d

def load_point_cloud(file_path):
    """
    Load the point cloud from a .ply file.
    """
    point_cloud = o3d.io.read_point_cloud(file_path)
    return point_cloud

def voxelize_point_cloud(point_cloud, voxel_size=0.05):
    """
    Voxelize the point cloud with a given voxel size.
    """
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(point_cloud, voxel_size=voxel_size)
    return voxel_grid

def save_voxel_grid(voxel_grid, output_file_path):
    """
    Save the voxel grid to a .ply file.
    """
    o3d.io.write_voxel_grid(output_file_path, voxel_grid)
    print(f"Voxel grid saved as {output_file_path}")

def display_point_cloud_and_voxelization(point_cloud, voxel_grid):
    """
    Display the original point cloud and the voxelized version.
    """
    # Create a visualization window
    o3d.visualization.draw_geometries([point_cloud], window_name="Original Point Cloud")

    # Visualize the voxel grid
    o3d.visualization.draw_geometries([voxel_grid], window_name="Voxelized Point Cloud")

def main():
    file_path = "ply_model.ply"  # Replace with your .ply file path
    output_voxel_file_path = "voxel_grid.ply"

    # Load the point cloud
    point_cloud = load_point_cloud(file_path)

    # Voxelize the point cloud
    voxel_grid = voxelize_point_cloud(point_cloud, voxel_size=0.01)

    save_voxel_grid(voxel_grid, output_voxel_file_path)

    # Display the original point cloud and its voxelization
    display_point_cloud_and_voxelization(point_cloud, voxel_grid)

if __name__ == "__main__":
    main()
