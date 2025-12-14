import pandas as pd
from usadata.cleaning import merge_data


def test_merge_data_returns_expected_dataframe():
	sensor_df = pd.DataFrame({
		"State": ["A", "A", "B"],
		"PM25_Yearly_Avg": [10, 20, 30]
	})

	state_df = pd.DataFrame({
		"States": ["A", "B", "C"]
	})

	# Call the function with DataFrames and get returned DataFrame
	result = merge_data(sensor_df, state_df)

	assert "Avg_PM25" in result.columns
	assert result.loc[result["States"] == "A", "Avg_PM25"].values[0] == 15
	assert result.loc[result["States"] == "B", "Avg_PM25"].values[0] == 30
	assert pd.isna(result.loc[result["States"] == "C", "Avg_PM25"].values[0])

