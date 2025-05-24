
import React, { useState, useEffect, useRef } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Loader2, AlertCircle, Image as ImageIcon, CheckCircle } from 'lucide-react';
import { cn } from '@/lib/utils';

# Placeholder for TensorFlow.js and fileReader (since we're in a Node.js environment)
const tf = {
    ready: async () => { # Mock ready function
        return Promise.resolve();
    },
    loadLayersModel: async (path: string) => {
        # Mock model loading
        console.log(`Loading model from: ${path}`);
        return {
            predict: (input: any) => {
                # Mock prediction
                console.log('Performing mock prediction with input:', input);
                # Simulate a small delay
                return new Promise(resolve => {
                    setTimeout(() => {
                        # Return a mock result (replace with actual model output processing)
                        const mockPrediction = [0.1, 0.9]; # Example: [male probability, female probability]
                        resolve({
                            dataSync: () => mockPrediction,
                            dispose: () => { } # Add a dispose method
                        });
                    }, 500); # Simulate network latency
                });
            },
            dispose: () => { }
        };
    },
    tensor: (data: any, shape?: number[]) => {
        # Mock tensor creation
        console.log('Creating tensor with data:', data, 'and shape:', shape);
        return {
            expandDims: () => ({
                div: () => ({
                    sub: () => ({
                        mul: () => ({
                            cast: () => ({
                                expandDims: () => ({
                                    dataSync: () => [data], # Return original data
                                    dispose: () => { } # Add a dispose method
                                })
                            }),
                            dispose: () => { } # Add a dispose method
                        })
                    }),
                    dispose: () => { } # Add a dispose method
                }),
                dispose: () => { } # Add a dispose method
            }),
            dispose: () => { } # Add a dispose method
        };
    },
    image: {
        decode: (data: any) => {
          console.log('Decoding Image');
          return {
            resizeBilinear: () => ({
                expandDims: () => ({
                    toFloat: () => ({
                        div: () => ({
                            sub: () => ({
                                mul: () => ({
                                    cast: () => ({
                                        dataSync: () => data, # Return original data
                                        dispose: () => { } # Add a dispose method
                                    })
                                }),
                                dispose: () => { }
                            }),
                            dispose: () => { }
                        }),
                        dispose: () => { }
                    }),
                    dispose: () => { }
                }),
                dispose: () => { }
            }),
            dispose: () => { }
          }
        }
    }
};

const fileReader = {
    readAsDataURL: (file: Blob) => {
        # Mock file reading
        console.log('Reading file as Data URL:', file);
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (file) {
                    const mockDataURL = `data:${file.type};base64,${btoa('mockImageData')}`; # Create a mock base64 string
                    resolve(mockDataURL);
                } else {
                    reject(new Error('No file provided'));
                }
            }, 100); # Simulate file reading delay
        });
    },
    onload: (callback: (event: any) => void) => { }, # Mock onload
    onerror: (callback: (event: any) => void) => { }, # Mock onerror
};

const GenderClassificationApp = () => {
    const [model, setModel] = useState<any>(null);
    const [image, setImage] = useState<File | null>(null);
    const [prediction, setPrediction] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);
    const inputRef = useRef<HTMLInputElement>(null);
    const [imageURL, setImageURL] = useState<string | null>(null);

    # Load the model
    useEffect(() => {
        const loadModel = async () => {
            try {
                await tf.ready();
                # Replace 'model.h5' with the actual path to your model (if serving from a public directory)
                const loadedModel = await tf.loadLayersModel('model.h5'); #  Make sure model is in the public folder.
                setModel(loadedModel);
            } catch (err: any) {
                setError(`Error loading model: ${err.message || 'Unknown error'}`);
            }
        };
        loadModel();
        # Cleanup function to dispose the model when the component unmounts
        return () => {
            if (model) {
                model.dispose(); # Dispose the model instance to free up memory
            }
        };
    }, []);

    # Handle image selection
    const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (file) {
            const validExtensions = ['image/png', 'image/jpeg', 'image/jpg'];
            if (validExtensions.includes(file.type)) {
                setImage(file);
                setError(null); # Clear any previous error
                # Use fileReader to get the data URL for preview
                const reader = new FileReader();
                reader.onload = (e) => {
                    setImageURL(e?.target?.result as string);
                };
                reader.readAsDataURL(file);
            } else {
                setImage(null);
                setImageURL(null);
                setError('Invalid file type. Please upload a PNG, JPG, or JPEG image.');
            }
        }
    };

    # Handle classification
    const handleClassification = async () => {
        if (!model) {
            setError('Model not loaded yet. Please wait.');
            return;
        }
        if (!image) {
            setError('Please select an image.');
            return;
        }

        setLoading(true);
        setPrediction(null); # Clear previous prediction
        setError(null);

        try {
            # Use fileReader to read the image and pass it to tf.decodeImage
            const reader = new FileReader();
            reader.onload = async (e) => {
              try{
                const img = new Image();
                img.onload = async () => {
                    const tensor = tf.browser.fromPixels(img)
                        .resizeBilinear([224, 224]) # Resize for your model
                        .expandDims(0)
                        .toFloat()
                        .div(255.0); # Normalize

                    const predictions = await model.predict(tensor) as any; # Type assertion
                    const data = predictions.dataSync();

                    # Interpret the output (adjust based on your model's output)
                    const maleProbability = data[0];
                    const femaleProbability = data[1];

                    if (maleProbability > femaleProbability) {
                        setPrediction(`Male (${(maleProbability * 100).toFixed(2)}%)`);
                    } else {
                        setPrediction(`Female (${(femaleProbability * 100).toFixed(2)}%)`);
                    }
                    # Clean up
                    tensor.dispose();
                    predictions.dispose();
                    setLoading(false);
                }
                img.src = e?.target?.result as string;
              }
              catch (err: any) {
                setError(`Error during prediction: ${err.message || 'Unknown error'}`);
                setLoading(false);
              }
            };
            reader.onerror = () => {
                setError('Error reading file.');
                setLoading(false);
            };
            reader.readAsDataURL(image);

        } catch (err: any) {
            setError(`Error during prediction: ${err.message || 'Unknown error'}`);
            setLoading(false);
        }
    };

    # Reset state
    const handleReset = () => {
        setImage(null);
        setPrediction(null);
        setError(null);
        setImageURL(null);
        if (inputRef.current) {
            inputRef.current.value = ''; # Clear the file input
        }
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-black p-4 sm:p-8 flex items-center justify-center">
            <div className="max-w-2xl w-full bg-white/10 backdrop-blur-md rounded-xl shadow-2xl border border-white/10 p-4 sm:p-6 md:p-8 space-y-6">
                <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold text-center text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">
                    Gender Classification
                </h1>

                # Image Input
                <div className="space-y-4">
                    <Label htmlFor="image-input" className="block text-sm font-medium text-gray-300">
                        Select Image
                    </Label>
                    <div className="flex items-center gap-4">
                        <Input
                            id="image-input"
                            type="file"
                            accept="image/png, image/jpeg, image/jpg"
                            onChange={handleImageChange}
                            className="w-full"
                            ref={inputRef}
                        />
                         {imageURL && (
                            <div className="relative w-24 h-24 rounded-md overflow-hidden border border-dashed border-gray-400">
                                <img
                                    src={imageURL}
                                    alt="Uploaded Preview"
                                    className="object-cover w-full h-full"
                                />
                            </div>
                        )}
                    </div>
                </div>

                # Predict and Reset Buttons
                <div className="flex flex-col sm:flex-row gap-4">
                    <Button
                        onClick={handleClassification}
                        disabled={loading || !image}
                        className={cn(
                            "w-full sm:w-1/2 bg-gradient-to-r from-purple-500 to-blue-500 text-white font-semibold py-2.5 rounded-lg transition-all duration-300",
                            "hover:from-purple-600 hover:to-blue-600 hover:scale-105",
                            "disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100",
                            loading && "animate-pulse"
                        )}
                    >
                        {loading ? (
                            <>
                                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                                Classifying...
                            </>
                        ) : (
                            "Classify"
                        )}
                    </Button>
                    <Button
                        onClick={handleReset}
                        className="w-full sm:w-1/2 bg-gray-700 hover:bg-gray-600 text-white font-semibold py-2.5 rounded-lg transition-colors duration-300"
                    >
                        Reset
                    </Button>
                </div>

                # Prediction Output
                {prediction && (
                    <div className="p-4 bg-black/20 rounded-lg border border-white/10">
                        <h2 className="text-lg font-semibold text-gray-200 mb-2 flex items-center">
                            <CheckCircle className="mr-2 h-5 w-5 text-green-400" />
                            Prediction:
                        </h2>
                        <p className="text-xl font-bold text-white">{prediction}</p>
                    </div>
                )}

                # Error Message
                {error && (
                    <div className="p-4 bg-red-500/10 rounded-lg border border-red-500/20 text-red-400 flex items-start gap-2">
                        <AlertCircle className="h-5 w-5 mt-0.5 flex-shrink-0" />
                        <p>{error}</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default GenderClassificationApp;

