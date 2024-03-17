from gradio_client import Client

client = Client("http://127.0.0.1:7865/")
result = client.predict(
				"Howdy!",	# str in 'parameter_12' Textbox component
				"Howdy!",	# str in 'parameter_13' Textbox component
				"Howdy!",	# str in 'parameter_14' Textbox component
				"Howdy!",	# str in 'parameter_15' Textbox component
				"Howdy!",	# str in 'parameter_16' Textbox component
				"Howdy!",	# str in 'parameter_17' Textbox component
				"Howdy!",	# str in 'parameter_18' Textbox component
				"Howdy!",	# str in 'parameter_19' Textbox component
				"Howdy!",	# str in 'parameter_20' Textbox component
				"Howdy!",	# str in 'parameter_21' Textbox component
				"Howdy!",	# str in 'parameter_22' Textbox component
				"Howdy!",	# str in 'parameter_23' Textbox component
				"Howdy!",	# str in 'parameter_24' Textbox component
				"Howdy!",	# str in 'parameter_25' Textbox component
				"Howdy!",	# str in 'parameter_26' Textbox component
				"Howdy!",	# str in 'parameter_27' Textbox component
				"Howdy!",	# str in 'parameter_28' Textbox component
				"Howdy!",	# str in 'parameter_29' Textbox component
				"Howdy!",	# str in 'parameter_30' Textbox component
				"Howdy!",	# str in 'parameter_31' Textbox component
				["Fooocus V2"],	# List[str] in 'Selected Styles' Checkboxgroup component
				"Quality",	# str in 'Performance' Radio component
				"704×1408 <span style=\"color: grey;\"> ∣ 1:2</span>",	# str in 'Aspect Ratios' Radio component
				1,	# int | float (numeric value between 1 and 32)
				"png",	# str in 'Output Format' Radio component
				"Howdy!",	# str in 'Seed' Textbox component
				0,	# int | float (numeric value between 0.0 and 30.0)
				1,	# int | float (numeric value between 1.0 and 30.0)
				"juggernautXL_v8Rundiffusion.safetensors",	# str (Option from: ['juggernautXL_v8Rundiffusion.safetensors'])
				"None",	# str (Option from: ['None', 'juggernautXL_v8Rundiffusion.safetensors'])
				0.1,	# int | float (numeric value between 0.1 and 1.0)
				True,	# bool in 'Enable' Checkbox component
				"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors'])
				-2,	# int | float (numeric value between -2 and 2)
				True,	# bool in 'Enable' Checkbox component
				"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors'])
				-2,	# int | float (numeric value between -2 and 2)
				True,	# bool in 'Enable' Checkbox component
				"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors'])
				-2,	# int | float (numeric value between -2 and 2)
				True,	# bool in 'Enable' Checkbox component
				"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors'])
				-2,	# int | float (numeric value between -2 and 2)
				True,	# bool in 'Enable' Checkbox component
				"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors'])
				-2,	# int | float (numeric value between -2 and 2)
				"Howdy!",	# str in 'parameter_53' Textbox component
				True,	# bool in 'Disable Preview' Checkbox component
				True,	# bool in 'Disable Intermediate Results' Checkbox component
				True,	# bool in 'Disable seed increment' Checkbox component
				0.1,	# int | float (numeric value between 0.1 and 3.0)
				0.1,	# int | float (numeric value between 0.1 and 3.0)
				0,	# int | float (numeric value between 0.0 and 1.0)
				1,	# int | float (numeric value between 1.0 and 30.0)
				"euler",	# str (Option from: ['euler', 'euler_ancestral', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ddim', 'uni_pc', 'uni_pc_bh2'])
				"normal",	# str (Option from: ['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'lcm', 'turbo'])
				-1,	# int | float (numeric value between -1 and 200)
				-1,	# int | float (numeric value between -1 and 200)
				-1,	# int | float (numeric value between -1 and 2048)
				-1,	# int | float (numeric value between -1 and 2048)
				-1,	# int | float (numeric value between -1 and 1.0)
				-1,	# int | float (numeric value between -1 and 1.0)
				True,	# bool in 'Mixing Image Prompt and Vary/Upscale' Checkbox component
				True,	# bool in 'Mixing Image Prompt and Inpaint' Checkbox component
				True,	# bool in 'Debug Preprocessors' Checkbox component
				True,	# bool in 'Skip Preprocessors' Checkbox component
				1,	# int | float (numeric value between 1 and 255)
				1,	# int | float (numeric value between 1 and 255)
				"joint",	# str (Option from: ['joint', 'separate', 'vae'])
				0,	# int | float (numeric value between 0.0 and 1.0)
				True,	# bool in 'Enabled' Checkbox component
				0,	# int | float (numeric value between 0 and 2)
				0,	# int | float (numeric value between 0 and 2)
				0,	# int | float (numeric value between 0 and 4)
				0,	# int | float (numeric value between 0 and 4)
				True,	# bool in 'Debug Inpaint Preprocessing' Checkbox component
				True,	# bool in 'Disable initial latent in inpaint' Checkbox component
				"None",	# str (Option from: ['None', 'v1', 'v2.5', 'v2.6'])
				0,	# int | float (numeric value between 0.0 and 1.0)
				0,	# int | float (numeric value between 0.0 and 1.0)
				True,	# bool in 'Enable Mask Upload' Checkbox component
				True,	# bool in 'Invert Mask' Checkbox component
				-64,	# int | float (numeric value between -64 and 64)
				True,	# bool in 'Save Metadata to Images' Checkbox component
				"fooocus",	# str in 'Metadata Scheme' Radio component
				"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image)
				"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image)
				"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image)
				"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image)
				fn_index=19
)
print( "result is ", result)