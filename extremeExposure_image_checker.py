import os
import numpy as np
from PIL import Image
import time
import shutil

# Adjusted limits for 4056x3040 images
MAX_FILE_SIZE_BYTES = 30 * 1024 * 1024  # Increased to 30MB for high-res images
MAX_DIMENSION = 5000  # Increased to handle 4056x3040
PROCESS_TIMEOUT = 15  # Slightly increased timeout for larger images

def analyze_image_intensity(image_path: str, black_tolerance: int = 5, white_tolerance: int = 250) -> str:
    """
    Analyzes if a given image is black, white, or normal.
    Returns: 'black', 'white', or 'normal'
    """
    filename = os.path.basename(image_path)
    
    try:
        # 1. File size check
        file_size = os.path.getsize(image_path)
        
        if file_size == 0:
            print(f"Warning: {filename} is 0 bytes. Classified as black.")
            return 'black'
            
        if file_size > MAX_FILE_SIZE_BYTES:
            print(f"Skipping: {filename} (Size: {file_size / 1024 / 1024:.2f} MB) - Exceeds max size.")
            return 'skip'

        # 2. Quick file read test
        try:
            with open(image_path, 'rb') as f:
                header = f.read(100)
            if len(header) < 10:
                return 'black'
        except (IOError, OSError):
            print(f"Error: Cannot read {filename}")
            return 'error'

        # 3. Process with PIL with timeout protection
        start_time = time.time()
        
        with Image.open(image_path) as img:
            # Get image dimensions
            width, height = img.size
            
            if width > MAX_DIMENSION or height > MAX_DIMENSION:
                print(f"Skipping: {filename} ({width}x{height}) - Dimensions too large")
                return 'skip'
            
            # Check timeout
            if time.time() - start_time > PROCESS_TIMEOUT:
                print(f"Timeout: {filename} - Taking too long to open")
                return 'skip'
            
            # Convert to grayscale
            img = img.convert('L')
            
            # Check timeout again
            if time.time() - start_time > PROCESS_TIMEOUT:
                print(f"Timeout: {filename} - Taking too long to convert")
                return 'skip'
            
            # Convert to numpy array and calculate average intensity
            img_array = np.array(img)
            average_intensity = np.mean(img_array)
            
            # Classification
            if average_intensity <= black_tolerance:
                status = 'black'
            elif average_intensity >= white_tolerance:
                status = 'white'
            else:
                status = 'normal'
            
            # Display results with color coding
            if status == 'black':
                print(f"⚫ [BLACK] {filename} - Avg intensity: {average_intensity:.2f}")
            elif status == 'white':
                print(f"⚪ [WHITE] {filename} - Avg intensity: {average_intensity:.2f}")
            else:
                print(f"✅ [NORMAL] {filename} - Avg intensity: {average_intensity:.2f}")
            
            return status

    except (IOError, OSError, Image.DecompressionBombError, Image.UnidentifiedImageError) as e:
        print(f"Error processing {filename}: {e}")
        return 'error'
    except MemoryError:
        print(f"Memory error processing {filename} - file too large")
        return 'error'
    except Exception as e:
        print(f"Unexpected error with {filename}: {e}")
        return 'error'

def create_folder(directory_path: str, folder_name: str) -> str:
    """Create a folder in the target directory"""
    folder_path = os.path.join(directory_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created {folder_name} folder: {folder_path}")
    return folder_path

def move_images(file_list: list, source_directory: str, dest_folder: str, folder_name: str):
    """Move images to the specified folder"""
    moved_count = 0
    failed_moves = []
    
    for filename in file_list:
        source_path = os.path.join(source_directory, filename)
        dest_path = os.path.join(dest_folder, filename)
        
        try:
            shutil.move(source_path, dest_path)
            print(f"MOVED: {filename} -> {folder_name}/")
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {filename}: {e}")
            failed_moves.append(filename)
    
    return moved_count, failed_moves

def check_directory_for_extreme_images(directory_path: str, black_tolerance: int = 5, white_tolerance: int = 250, auto_move: bool = False):
    """
    Iterates through all JPG files in a directory and reports black/white images.
    """
    print(f"--- Image Analyzer Tool Initialized ---")
    print(f"Target Directory: {directory_path}")
    print(f"Black Tolerance (Max Avg Intensity): {black_tolerance}")
    print(f"White Tolerance (Min Avg Intensity): {white_tolerance}")
    print(f"Max File Size to Process: {MAX_FILE_SIZE_BYTES / 1024 / 1024:.2f} MB")
    print(f"Max Dimension: {MAX_DIMENSION}px")
    print(f"Auto-move images: {'YES' if auto_move else 'NO'}")
    print("-" * 60)

    black_files = []
    white_files = []
    processed_count = 0
    error_count = 0
    skip_count = 0
    
    if not os.path.exists(directory_path):
        print(f"🚨 ERROR: Directory not found or inaccessible: {directory_path}")
        return

    # Get all JPG files first to show progress
    jpg_files = [f for f in os.listdir(directory_path) 
                if f.lower().endswith(('.jpg', '.jpeg'))]
    
    total_files = len(jpg_files)
    print(f"Found {total_files} JPG files to process...")
    
    if total_files == 0:
        print("No JPG files found in directory.")
        return

    start_time = time.time()
    
    for filename in jpg_files:
        processed_count += 1
        
        full_path = os.path.join(directory_path, filename)
        
        try:
            result = analyze_image_intensity(full_path, black_tolerance, white_tolerance)
            
            if result == 'black':
                black_files.append(filename)
            elif result == 'white':
                white_files.append(filename)
            elif result == 'skip':
                skip_count += 1
            elif result == 'error':
                error_count += 1
                
        except KeyboardInterrupt:
            print(f"\n⚠️ Processing interrupted by user")
            break
        except Exception as e:
            error_count += 1
            print(f"[ERROR] {filename}: {e}")

        # Progress reporting
        if processed_count % 50 == 0 or processed_count == total_files:
            elapsed = time.time() - start_time
            rate = processed_count / elapsed if elapsed > 0 else 0
            remaining = (total_files - processed_count) / rate if rate > 0 else 0
            print(f"Progress: {processed_count}/{total_files} "
                  f"({processed_count/total_files*100:.1f}%) - "
                  f"{rate:.1f} files/sec - "
                  f"Found: {len(black_files)} black, {len(white_files)} white")

    # Final summary
    total_time = time.time() - start_time
    print("-" * 60)
    print(f"--- Analysis Complete ---")
    print(f"Total files processed: {processed_count}")
    print(f"Processing time: {total_time:.1f}s ({processed_count/max(total_time,0.1):.1f} files/sec)")
    print(f"Black images found: {len(black_files)}")
    print(f"White images found: {len(white_files)}")
    print(f"Normal images: {processed_count - len(black_files) - len(white_files) - skip_count - error_count}")
    print(f"Files skipped: {skip_count}")
    print(f"Errors encountered: {error_count}")
    
    # Create folders and move images if any were found
    if black_files or white_files:
        if black_files:
            print(f"\n⚫ Black images found ({len(black_files)}):")
            for file in black_files[:10]:  # Show first 10 only
                print(f"  - {file}")
            if len(black_files) > 10:
                print(f"  ... and {len(black_files) - 10} more")
        
        if white_files:
            print(f"\n⚪ White images found ({len(white_files)}):")
            for file in white_files[:10]:  # Show first 10 only
                print(f"  - {file}")
            if len(white_files) > 10:
                print(f"  ... and {len(white_files) - 10} more")
        
        # Auto-move functionality
        if auto_move:
            if black_files:
                black_folder = create_folder(directory_path, "BLACK")
                moved_black, failed_black = move_images(black_files, directory_path, black_folder, "BLACK")
                print(f"\n📁 Moved {moved_black}/{len(black_files)} black images to: {black_folder}")
            
            if white_files:
                white_folder = create_folder(directory_path, "WHITE")
                moved_white, failed_white = move_images(white_files, directory_path, white_folder, "WHITE")
                print(f"📁 Moved {moved_white}/{len(white_files)} white images to: {white_folder}")
        else:
            # Ask user if they want to move the files
            if black_files or white_files:
                move_choice = input(f"\nMove images to folders? (b=black only, w=white only, a=all, n=none): ").lower().strip()
                
                if move_choice in ['b', 'a'] and black_files:
                    black_folder = create_folder(directory_path, "BLACK")
                    moved_black, failed_black = move_images(black_files, directory_path, black_folder, "BLACK")
                    print(f"\n📁 Moved {moved_black}/{len(black_files)} black images to: {black_folder}")
                
                if move_choice in ['w', 'a'] and white_files:
                    white_folder = create_folder(directory_path, "WHITE")
                    moved_white, failed_white = move_images(white_files, directory_path, white_folder, "WHITE")
                    print(f"📁 Moved {moved_white}/{len(white_files)} white images to: {white_folder}")
        
        # Save lists to files
        timestamp = int(time.time())
        if black_files:
            black_list_file = f"black_images_{timestamp}.txt"
            with open(black_list_file, 'w') as f:
                for file in black_files:
                    f.write(file + '\n')
            print(f"📝 Black list saved to: {black_list_file}")
        
        if white_files:
            white_list_file = f"white_images_{timestamp}.txt"
            with open(white_list_file, 'w') as f:
                for file in white_files:
                    f.write(file + '\n')
            print(f"📝 White list saved to: {white_list_file}")
        
    else:
        print("🎉 No black or white images were found in the directory.")

if __name__ == "__main__":
    target_directory = "."
    black_threshold = 5
    white_threshold = 250  # Adjust this as needed
    
    try:
        # Configuration options
        print("⚡ Image Analyzer - Black & White Detection")
        print(f"Default thresholds: Black ≤ {black_threshold}, White ≥ {white_threshold}")
        
        change_thresholds = input("Change thresholds? (y/n): ").lower().strip()
        if change_thresholds == 'y':
            try:
                black_threshold = int(input(f"Black tolerance (default {black_threshold}): ") or black_threshold)
                white_threshold = int(input(f"White tolerance (default {white_threshold}): ") or white_threshold)
            except ValueError:
                print("Using default thresholds")
        
        auto_move = input("Auto-move images to folders? (y/n): ").lower().strip() == 'y'
        
        check_directory_for_extreme_images(target_directory, black_threshold, white_threshold, auto_move)
            
    except KeyboardInterrupt:
        print("\n🚨 Program terminated by user")
    except Exception as e:
        print(f"🚨 Fatal error: {e}")
