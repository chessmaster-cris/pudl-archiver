"""Metadata and operational constants."""

from typing import Any

from pudl.metadata.constants import CONTRIBUTORS, LICENSES

# To add a new contributor, follow the following format to add an entry to the
# ADDL_CONTRIBUTORS dictionary below formatted like this:
#     "name-shorthand": {
#         "title": "Catalyst Cooperative",
#         "email": "pudl@catalyst.coop",
#         "path": "https://catalyst.coop",
#         "role": "publisher",
#         "zenodo_role": "distributor",
#         "organization": "Catalyst Cooperative",
#         "orcid": "0000-1234-5678-9101"
#     }
# Note that the only required fields are title (your name) and path
# (e.g., a link to your Github account, your ORCID site or a personal webpage), but
# filling other fields is strongly encouraged!
ADDL_CONTRIBUTORS: dict[str, dict[str, str]] = {}

NON_PUDL_SOURCES: dict[str, Any] = {
    "doelead": {
        "title": "DOE LEAD -- Low Income Energy Affordability Data",
        "path": "https://www.energy.gov/scep/low-income-energy-affordability-data-lead-tool",
        "description": (
            "This archive includes the data behind the Department of Energy's (DOE) "
            "Low Income Energy Affordability Data (LEAD) tool. The LEAD tool is an "
            "online, interactive platform that helps users make data-driven decisions "
            "on energy goals and program planning by improving their understanding of "
            "low-income and moderate-income household energy characteristics. The LEAD "
            "Tool offers the ability to select and combine geographic areas (state, "
            "county, city and census tract) into one customized group so users can see "
            "the total area for their customized geographies (e.g., specific service "
            "territories)."
        ),
        "working_partitions": {"years": [2018, 2022]},
        "keywords": sorted(
            {"doe", "lead", "low income", "energy affordability", "energy burden"}
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "eiacbecs": {
        "title": "EIA CBECS -- Commercial Buildings Energy Consumption Survey",
        "path": "https://www.eia.gov/consumption/commercial/",
        "description": (
            "The Commercial Buildings Energy Consumption Survey (CBECS) is a national "
            "sample survey that collects information on the stock of U.S. commercial "
            "buildings, including their energy-related building characteristics and "
            "energy usage data (consumption and expenditures). Commercial buildings "
            "include all buildings in which at least half of the floorspace is used for "
            "a purpose that is not residential, industrial, or agricultural. By this "
            "definition, CBECS includes building types that might not traditionally be "
            "considered commercial, such as schools, hospitals, correctional "
            "institutions, and buildings used for religious worship, in addition to "
            "traditional commercial buildings such as stores, restaurants, warehouses, "
            "and office buildings."
        ),
        "working_partitions": {
            "years": [
                2003,
                2012,
                2018,
            ]  # there are PDF only versions for 1999, 1995 and 1992
        },
        "keywords": sorted(
            {"eia", "energy", "cbecs", "consumption", "buildings", "commercial"}
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "eianems": {
        "title": "EIA NEMS -- National Energy Modeling System",
        "path": "https://github.com/EIAgov/NEMS",
        "description": (
            "The National Energy Modeling System (NEMS) is a long-term energy-economy "
            "modeling system of U.S. energy markets. The model is used to project "
            "production, imports, exports, conversion, consumption, and prices of "
            "energy, subject to user-defined assumptions. The assumptions encompass "
            "macroeconomic and financial factors, world energy markets, resource "
            "availability and costs, behavioral and technological choice criteria, "
            "technology characteristics, and demographics. EIA's Office of Energy "
            "Analysis develops and maintains NEMS to support the Annual Energy Outlook "
            "(AEO). The NEMS model was open sourced in 2024 for the 2023 version of "
            "AEO. Beyond the model itself, the inputs for NEMS contains valuable data."
        ),
        "working_partitions": {"years": [2023]},
        "keywords": sorted({"eia", "nems", "aeo"}),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "eiamecs": {
        "title": "EIA MECS -- Manufacturing Energy Consumption Survey",
        "path": "https://www.eia.gov/consumption/manufacturing/data/2018/",
        "description": (
            "EIA Form 846 A and B is more commonly known as the Manufacturing Energy "
            "Consumption Survey (MECS). MECS is a national sample survey that collects "
            "information on the stock of U.S. manufacturing establishment, their "
            "energy-related building characteristics, and their energy consumption "
            "and expenditures. MECS is conducted every four years."
        ),
        "working_partitions": {
            "years": [1991, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
        },
        "keywords": sorted(
            {
                "eia",
                "manufacturing",
                "MECS",
            }
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "eiarecs": {
        "title": "EIA RECS -- Residential Energy Consumption Survey",
        "path": "https://www.eia.gov/consumption/residential/",
        "description": (
            "EIA administers the Residential Energy Consumption Survey (RECS) to a "
            "nationally representative sample of housing units. Traditionally, "
            "specially trained interviewers collect energy characteristics on the "
            "housing unit, usage patterns, and household demographics. For the 2020 "
            "survey cycle, EIA used Web and mail forms to collect detailed information "
            "on household energy characteristics. This information is combined with "
            "data from energy suppliers to these homes to estimate energy costs and "
            "usage for heating, cooling, appliances and other end uses — information "
            "critical to meeting future energy demand and improving efficiency and "
            "building design."
        ),
        "working_partitions": {
            "years": [2009, 2015, 2020]  # Only PDFs: 1993, 1997, 2001, 2005
        },
        "keywords": sorted(
            {
                "eia",
                "recs",
                "residential",
                "household",
                "building",
                "energy",
                "consumption",
            }
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "usgsuswtdb": {
        "title": "USGS USWTDB - U.S. Wind Turbine Database",
        "path": "https://energy.usgs.gov/uswtdb/",
        "description": (
            "The United States Wind Turbine Database (USWTDB) provides the locations "
            "of land-based and offshore wind turbines in the United States, "
            "corresponding wind project information, and turbine technical "
            "specifications. Wind turbine records are collected and compiled from "
            "various public and private sources, digitized and position-verified from "
            "aerial imagery, and quality checked. The USWTDB is available for download "
            "in a variety of tabular and geospatial file formats, to meet a range of "
            "user/software needs. Dynamic web services are available for users that wish "
            "to access the USWTDB as a Representational State Transfer Services (RESTful) "
            "web service."
        ),
        "working_partitions": {
            "year_months": [
                "2018-04",
                "2018-07",
                "2018-10",
                "2019-01",
                "2019-04",
                "2019-07",
                "2019-10",
                "2020-01",
                "2020-04",
                "2020-05",
                "2020-07",
                "2020-10",
                "2021-01",
                "2021-04",
                "2021-07",
                "2021-11",
                "2022-01",
                "2022-04",
                "2022-07",
                "2022-10",
                "2023-01",
                "2023-05",
                "2023-11",
                "2024-05",
                "2024-11",
            ]  # these are almost year_quarters but not quite....
        },
        "keywords": sorted(
            {
                "usgs",
                "uswtdb",
                "wind",
                "wind turbines",
                "spatial",
                "gis",
                "geospatial",
                "geometry",
                "renewable",
                "electricity",
                "generation",
                "energy",
            }
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "usgsuspvdb": {
        "title": "USGS USPVDB -- U.S. Large-Scale Solar Photovoltaic Database",
        "path": "https://energy.usgs.gov/uspvdb/",
        "description": (
            "The United States Large-Scale Solar Photovoltaic Database (USPVDB) provides "
            "the locations and array boundaries of U.S. ground-mounted photovoltaic (PV) "
            "facilities with capacity of 1 megawatt or more. It includes corresponding PV "
            "facility information, including panel type, site type, and initial year of "
            "operation. The creation of this database was jointly funded by the U.S. "
            "Department of Energy (DOE) Solar Energy Technologies Office (SETO) via the "
            "Lawrence Berkeley National Laboratory (LBNL) Energy Markets and Policy "
            "Department, and the U.S. Geological Survey (USGS) Energy Resources Program. "
            "The PV facility records are collected from the U.S. Energy Information "
            "Administration (EIA), position-verified and digitized from aerial imagery, "
            "and checked for quality. EIA facility data are supplemented with additional "
            "attributes obtained from public sources."
        ),
        "working_partitions": {"years": [2023, 2024]},
        "keywords": sorted(
            {
                "usgs",
                "uspvdb",
                "solar",
                "pv",
                "photovoltaic",
                "doe",
                "seto",
                "lbnl",
                "spatial",
                "gis",
                "geospatial",
                "geometry",
                "renewable",
                "electricity",
                "generation",
                "energy",
            }
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "epaegrid": {
        "title": "EPA eGRID -- Emissions & Generation Resource Integrated Database",
        "path": "https://www.epa.gov/egrid",
        "description": (
            "The Emissions & Generation Resource Integrated Database (eGRID) is a "
            "comprehensive source of data from EPA's Clean Air Power Sector Programs on "
            "the environmental characteristics of almost all electric power generated in "
            "the United States. The data includes emissions, emission rates, generation, "
            "heat input, resource mix, and many other attributes. eGRID is typically used "
            "for greenhouse gas registries and inventories, carbon footprints for "
            "electricity purchases, consumer information disclosure, emission inventories "
            "and standards, power market changes, and avoided emission estimates."
        ),
        "working_partitions": {"years": [2018, 2019, 2020, 2021, 2022, 2023]},
        "keywords": sorted(
            {
                "epa",
                "egrid",
                "emissions",
                "greenhouse gas",
                "heat input",
                "resource mix",
                "carbon footprint",
                "avoided emissions",
            }
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "doeiraec": {
        "title": "DOE -- IRA Energy Community Data Layers",
        "path": "https://edx.netl.doe.gov/dataset/ira-energy-community-data-layers",
        "description": (
            "An IRA Energy Community refers to areas designated under the U.S. Inflation Reduction "
            "Act (IRA) as eligible for special incentives to promote clean energy development. These "
            "communities are typically regions impacted by the transition away from fossil fuels, "
            "such as those with closed coal mines or retired coal-fired power plants. The designation "
            "aims to boost local economies and job creation by attracting renewable energy projects "
            "like wind, solar, and battery storage, often offering enhanced tax credits to developers "
            "working in these areas."
            "This source contains data for two types of potentially qualifying energy communities: 1) "
            "Census tracts and directly adjoining tracts that have had coal mine closures since 1999 "
            "or coal-fired electric generating unit retirements since 2009. These census tracts qualify "
            "as energy communities. 2) Metropolitan statistical areas (MSAs) and non-metropolitan statistical "
            "areas (non-MSAs) that are energy communities for 2023 and 2024, along with their fossil "
            "fuel employment (FFE) status."
        ),
        "working_partitions": {"years": [2024]},
        "keywords": sorted(
            {
                "energy community",
                "coal",
                "mines",
                "closure",
                "ira",
            }
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "epadcejp": {
        "title": "EPA -- Disadvantaged Community Energy Justice Program",
        "path": "https://www.epa.gov/ejscreen/technical-information-and-data-downloads",
        "description": (
            "This dataset denotes whether a region is considered a disadvantaged community based on "
            "the EPA's Energy Justice Program. An EPA Disadvantaged Community under the Energy Justice "
            "Program is identified based on four key factors: environmental challenges like high pollution "
            "exposure, economic hardships such as low income or high unemployment, social vulnerabilities "
            "including health disparities and minority status, and geographic disadvantages in rural, urban, "
            "or remote areas. These criteria ensure that support is directed to communities facing systemic "
            "inequities and the greatest need for clean energy and environmental investments."
        ),
        "working_partitions": {},  # not 100% sure
        "keywords": sorted(
            {"energy", "community", "ira", "environment", "justice", "epa"}
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
    "epamats": {
        "title": "EPA -- Mercury and Air Toxics Standards",
        "path": "https://www.epa.gov/stationary-sources-air-pollution/mercury-and-air-toxics-standards",
        "description": (
            "The EPA Mercury and Air Toxics Standards (MATS) dataset provides detailed information on emissions "
            "of hazardous air pollutants, specifically mercury and other toxic substances, from power plants in "
            "the United States. Established by the U.S. Environmental Protection Agency (EPA) under the Clean Air "
            "Act, MATS aims to reduce air pollution and its associated health risks by setting limits on the "
            "emissions of mercury, arsenic, acid gases, and other pollutants from coal- and oil-fired power "
            "plants. The dataset typically includes metrics such as emission levels, compliance testing results, "
            "facility locations, and operational data. It serves as a critical resource for policymakers, "
            "researchers, and environmental organizations to assess the effectiveness of pollution control "
            "measures, monitor compliance, and evaluate the environmental and public health impacts of power "
            "plant emissions."
        ),
        "working_partitions": {
            "years": [
                1990,
                1991,
                1992,
                1993,
                1994,
                1995,
                1996,
                1997,
                1998,
                1999,
                2000,
                2001,
                2002,
                2003,
                2004,
                2005,
                2006,
                2007,
                2008,
                2009,
                2010,
                2011,
                2012,
                2013,
                2014,
                2015,
                2016,
                2017,
                2018,
                2019,
                2020,
                2021,
                2022,
            ]
        },  # not 100% sure on years
        "keywords": sorted(
            {"mercury", "toxics", "standards", "air", "environment", "epa"}
        ),
        "license_raw": LICENSES["us-govt"],
        "license_pudl": LICENSES["cc-by-4.0"],
        "contributors": [CONTRIBUTORS["catalyst-cooperative"]],
    },
}
